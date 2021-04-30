print('Start GW AI speaker')

import speech_recognition as sr
#for tts
import pyttsx3
#for play sound-file
from playsound import playsound
#for Mic recording
import sounddevice as sd
from scipy.io.wavfile import write

def Saying(msg):
    engine = pyttsx3.init()  # 보이스엔진 초기화
    # voices = engine.getProperty('voices')
    # volume = engine.getProperty('volume')
    # rate = engine.getProperty('rate')
    # print('rate = ',rate)
    engine.setProperty('rate', 170)
    engine.say(msg)
    engine.runAndWait()

r = sr.Recognizer()
"""PART 1 : Greeting"""
msg = '명령하세요'
Saying(msg)

"""Part 2 : Speech Recognition from Mic."""
# print(sr.Microphone.list_microphone_names())
mic = sr.Microphone(device_index=1) #'Microsoft ???? - Input'
with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
"""
playsound('rfr.wav')

file_input = sr.AudioFile('rfr.wav')
with file_input as source:
    # r.adjust_for_ambient_noise(source)
    audio = r.record(source)
# fs = 44100  # Sample rate
# seconds = 3  # Duration of recording

# myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
# sd.wait()  # Wait until recording is finished
# write('output.wav', fs, myrecording)  # Save as WAV file 
"""
res = r.recognize_sphinx(audio, language="ko-KR") #'ko-KR' en-US
# res = r.recognize_google(audio, language="ko-KR") #'ko-KR' en-US
print('Result : ', res)
Saying(res)