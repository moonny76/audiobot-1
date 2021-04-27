from gtts import gTTS
from io import BytesIO

import speech_recognition as sr

print('<< Show Sound Device List >>\n', sr.Microphone.list_microphone_names())

cur_weather = '맑음'
next_weather = '더 맑음'
text = '현재 날씨는 {}이며 내일 날씨는 {} 입니다.'.format(cur_weather, next_weather)

tts = gTTS(text=text, lang='ko')

out_file_name = 'test.mp3'
tts.save(out_file_name)

import pygame

freq = 24000    # sampling rate, 44100(CD), 16000(Naver TTS), 24000(google TTS)
bitsize = -16   # signed 16 bit. support 8,-8,16,-16
channels = 1    # 1 is mono, 2 is stereo
buffer = 2048   # number of samples (experiment to get right sound)

# default : pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
pygame.mixer.init(freq, bitsize, channels, buffer)
pygame.mixer.music.load(out_file_name)
pygame.mixer.music.play()

clock = pygame.time.Clock()
while pygame.mixer.music.get_busy():
    clock.tick(30)
pygame.mixer.quit()   