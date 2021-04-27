from gtts import gTTS
import yfinance as yf
import numpy as np
import speech_recognition as sr


r = sr.Recognizer()
print(sr.Microphone.list_microphone_names())

mic = sr.Microphone(device_index=0) #'Microsoft ???? - Input'
with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
res = r.recognize_google(audio)
# res = r.recognize_sphinx(audio)
print('Result : ', res)

"""
item_stock = yf.Ticker('TSLA')
price = item_stock.history(period='1d')
cur_price = np.round(price['Close'].iloc[-1],1)
open_price = np.round(price['Open'].iloc[-1],1)
text = '현재 Tesla 주가는 {}이며 시초가는 {} 였습니다.'.format(cur_price, open_price)

tts = gTTS(text=text, lang='ko')
tts.save('hello.mp3')

import pygame

music_file = "hello.mp3"   # mp3 or mid file


freq = 24000    # sampling rate, 44100(CD), 16000(Naver TTS), 24000(google TTS)
bitsize = -16   # signed 16 bit. support 8,-8,16,-16
channels = 1    # 1 is mono, 2 is stereo
buffer = 2048   # number of samples (experiment to get right sound)

# default : pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
pygame.mixer.init(freq, bitsize, channels, buffer)
pygame.mixer.music.load(music_file)
pygame.mixer.music.play()

clock = pygame.time.Clock()
while pygame.mixer.music.get_busy():
    clock.tick(30)
pygame.mixer.quit()    
"""