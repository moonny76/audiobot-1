import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init()  
engine.setProperty('rate', 170)
#print(sr.Microphone.list_microphone_names())

def Saying(msg):
    print('TTS: ', msg)
    engine.say(msg)
    engine.runAndWait()
    
def speak2txt(audio):
    try:
        txt = r.recognize_google(audio, language="ko-KR") #'ko-KR' en-US
    except sr.RequestError:
        txt = 'Fail'
        print('Translate Fail')
    except sr.UnknownValueError:
        txt = 'Fail'
        print('Translate Fail')
    return txt

r = sr.Recognizer()
mic = sr.Microphone(device_index=2) 

while True:
    Saying('I will follow you')
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    Saying('On process')
    
    while speak2txt(audio) == 'Fail':
        print('wait voice..')
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

    with open("mic-results.wav", "wb") as f:
        f.write(audio.get_wav_data())
    Saying('Saved your word')
    
    res = r.recognize_google(audio, language="ko-KR") #'ko-KR' en-US
    while len(res) == 0:
        Saying('I will follow you')
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        Saying('On process')
        res = r.recognize_google(audio, language="ko-KR") #'ko-KR' en-US
        
    print('Result : ', res)
    Saying(res)

    import os
    os.system('aplay mic-results.wav')

