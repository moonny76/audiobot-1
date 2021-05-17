#from gtts import gTTS
import pyttsx3
from selenium import webdriver # python3 -m pip install selenium

print('start')

# part 1. news scrawl
# sudo apt-get install chromium-chromdriver
browser=webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
#driver=webdriver.Chrome('./chromedriver')

url='https://news.naver.com'
browser.get(url)
depth1=browser.find_element_by_id('today_main_news')
depth2=depth1.find_element_by_class_name('hdline_article_list')
depth3=depth2.find_elements_by_tag_name('li')

n=0
#linkd={}
for child in depth3:
   print('This is {}th headline\n'.format(n+1))
   print(child.text)
   #fname='article'+str(n+1)+'.txt'
   # link for each headline
#   linkd[n]=child.find_element_by_class_name('hdline_article_tit').get_attribute('href')  
#   print(linkd[n])
   
   f=open('headline.txt','a+',encoding='utf-8')
   f.write(child.text)
   
   n=n+1

f.close()

# part 2, tts
def Saying(msg):
   engine=pyttsx3.init()
   engine.setProperty('rate',170)
   engine.say(msg)
   engine.runAndWait()

f2=open('headline.txt','r',encoding='utf-8')
txt=f2.read()
f2.close()

Saying(txt)
#for child in depth3:
   #print(child.text)
   #Saying(child.text)

browser.quit()
