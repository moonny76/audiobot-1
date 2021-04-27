print('Start to test voice recognition')

import speech_recognition as sr
sr.__version__

r = sr.Recognizer()

"""
Part 1 : Speech Recognition from File
"""
# file_input = sr.AudioFile('harvard.wav')
# file_input = sr.AudioFile('jackhammer.wav')
file_input = sr.AudioFile('man.wav')
with file_input as source:
    audio = r.record(source)

print(type(audio))
out_google = r.recognize_google(audio)
out_sphinx = r.recognize_sphinx(audio) #, language='en-US', show_all=False)

print('From Google : ', out_google)
print('From Sphinx : ', out_sphinx)

"""
Part 2 : Speech Recognition from Mic.
"""
"""
print(sr.Microphone.list_microphone_names())
mic = sr.Microphone(device_index=0) #'Microsoft ???? - Input'
with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
# res = r.recognize_google(audio)
res = r.recognize_sphinx(audio)
print('Result : ', res)
"""