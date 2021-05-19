from mty_media_bot.service.talk_back import TalkBackRecorder, TalkBackPlayer, StreamRecognizer


class Word:
    def __init__(self, korean_word, english_word):
        self.korean_word = korean_word
        self.english_word = english_word


class Bot:
    def __init__(self, name, speaker_on=True):
        self.name = name
        self.speak_num = 0
        self.speaker_on = speaker_on
        self.actions = {}

    def add_command(self, command):
        for word in command.get_word():
            self.actions[word] = command

    def speak(self, message):
        self.speak_num += 1
        print(self.name, " : ", message)
        voice_file = f'resource/voice/{self.name}_{self.speak_num}.mp3'
        if self.speaker_on:
            TalkBackRecorder(voice_file).record(message)
            TalkBackPlayer(voice_file).play()

    def listen(self):
        try:
            stream_recognizer = StreamRecognizer()
            kr_text = stream_recognizer.recognize()
            self.speak(f"{kr_text} 라고")
            en_text = stream_recognizer.recognize(lang="en")
            print(self.name, " recognized : ", kr_text, "/", en_text)
            return Word(kr_text, en_text)
        except Exception as e:
            print(e)
            return None

    def process(self, word):
        for command_word in self.actions.keys():
            if command_word in word.korean_word or command_word in word.english_word:
                self.actions[command_word].execute(word)
                return True
        return False


class Assistant(Bot):
    pass


class Friend(Bot):
    pass
