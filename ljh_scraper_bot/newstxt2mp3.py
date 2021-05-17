from gtts import gTTS

# part 1. generate headline.mpe
f2=open('headline.txt','r',encoding='utf-8')
hdline_txt=f2.read()
f2.close()

tts = gTTS(text=hdline_txt, lang='ko', slow=False)
tts.save('headline.mp3')


# part 2. generate mp3 of each headline article
n=0
for n in range(5):
   fname='article'+str(n+1)
   f=open(fname+'.txt','r',encoding='utf-8')
   news_art=f.read()
   f.close()

   tts = gTTS(text=news_art, lang='ko', slow=False)
   tts.save(fname+'.mp3')

   n=n+1
