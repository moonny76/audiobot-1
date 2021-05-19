import os
import unittest
from abc import abstractmethod


class Recorder:

    def __init__(self, file):
        self.file = file

    @abstractmethod
    def record(self, message):
        pass


class TalkBackRecorder(Recorder):

    def record(self, message):
        from gtts import gTTS
        tts = gTTS(text=message, lang='ko')
        tts.save(self.file)
        return self.file


class Player:

    def __init__(self, file):
        self.file = file

    @abstractmethod
    def play(self):
        pass


class TalkBackPlayer(Player):

    def play(self):
        from audioplayer import AudioPlayer
        AudioPlayer(self.file).play(block=True)


class PygamePlayer(Player):

    def play(self):
        from pydub import AudioSegment
        wav_file_name = self.file.replace('.mp3', '.wav')
        audio = AudioSegment.from_mp3(self.file)
        audio.export(out_f=wav_file_name, format="wav")

        from pygame import mixer
        mixer.init()
        mixer.music.load(wav_file_name)
        mixer.music.play()


class PygletPlayer(Player):

    def play(self):
        import pyglet
        music = pyglet.resource.media(self.file)
        music.play()
        pyglet.app.run()


def talk_back_gtts(text, lang='ko'):
    tts_file_name = "talk_back.mp3"
    TalkBackRecorder(tts_file_name).record(text)
    TalkBackPlayer(tts_file_name).play()
    return tts_file_name


speak_functions = {
    'gtts': talk_back_gtts
}


def speak(text, type='gtts', lang='ko'):
    talk_back = speak_functions[type]
    return talk_back(text)


class Recognizer:

    @abstractmethod
    def recognize(self, message):
        pass


class FileRecognizer(Recognizer):
    def __init__(self, file):
        self.file = file

    def recognize(self, lang='ko'):
        from pydub import AudioSegment
        wav_file_name = self.file.replace('.mp3', '.wav')
        audio = AudioSegment.from_mp3(self.file)
        print(type(audio))
        audio.export(out_f=wav_file_name, format="wav")

        import speech_recognition as sr
        audio_file = sr.AudioFile(wav_file_name)
        recognizer = sr.Recognizer()
        with audio_file as source:
            audio_data = recognizer.record(source)
        os.remove(wav_file_name)
        if lang == 'ko':
            return recognizer.recognize_google(audio_data=audio_data, language="ko-KR")
        else:
            return recognizer.recognize_google(audio_data=audio_data, language="en-US")


class StreamRecognizer(Recognizer):

    def __init__(self):
        self.audio = None

    def recognize(self, lang='ko'):
        import speech_recognition as sr
        recognizer = sr.Recognizer()
        if self.audio is None:
            with sr.Microphone() as source:
                print("Listening to ...")
                self.audio = recognizer.listen(source, phrase_time_limit=5)
            print("Done")

        if lang == 'ko':
            return recognizer.recognize_google(audio_data=self.audio, language="ko-KR")
        else:
            return recognizer.recognize_google(audio_data=self.audio, language="en-US")


def recognize_mp3(file_name, lang='ko'):
    return FileRecognizer(file_name).recognize(lang=lang)

def recognize_stream(lang='ko'):
    return StreamRecognizer().recognize(lang=lang)

recognize_functions = {
    'mp3': recognize_mp3,
    'stream': recognize_stream
}


def recognize(file, type="mp3"):
    return recognize_functions[type](file)


class TTSTest(unittest.TestCase):
    def test_speak_gtts(self):
        text = "안녕하세요, 여러분. 파이썬으로 노는 것은 재미있습니다!!!"
        tts_file_name = speak(text)
        self.assertTrue(os.path.exists(tts_file_name))
        self.assertTrue(os.path.getsize(tts_file_name) > 0)
        os.remove(tts_file_name)

    def test_recognize_mp3(self):
        text = "안녕하세요"
        tts_file_name = speak(text)
        actual_text = recognize(tts_file_name)
        self.assertEqual(text, actual_text)
        os.remove(tts_file_name)

    def test_recognize_stream(self):
        text = "안녕하세요"
        actual_text = recognize_stream()
        self.assertEqual(text, actual_text)

################################################################################

if __name__ == "__main__":
    unittest.main()
