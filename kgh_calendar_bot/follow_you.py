import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init()  
engine.setProperty('rate', 170)
#print(sr.Microphone.list_microphone_names())

def Saying(msg):
    print(msg)
    engine.say(msg)
    engine.runAndWait()

r = sr.Recognizer()
mic = sr.Microphone(device_index=2) 

while True:
    Saying('I will follow you')
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    Saying('On process')

    with open("mic-results.wav", "wb") as f:
        f.write(audio.get_wav_data())
    Saying('Saved your word')

    res = r.recognize_google(audio, language="ko-KR") #'ko-KR' en-US
    print('Result : ', res)
    Saying(res)

    import os
    os.system('aplay mic-results.wav')

