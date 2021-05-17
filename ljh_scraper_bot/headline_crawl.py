from selenium import webdriver # python3 -m pip install selenium
import time

print('start')

# part 1. news scrawl
# sudo apt-get install chromium-chromdriver
# browser=webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
browser=webdriver.Chrome('C:\Python\chromedriver')

url='https://news.naver.com'

browser.get(url)
time.sleep(5)
depth1=browser.find_element_by_id('today_main_news')
depth2=depth1.find_element_by_class_name('hdline_article_list')
depth3=depth2.find_elements_by_tag_name('li')

n=0
linkd={}
for child in depth3:
   print('This is {}th headline'.format(n+1))
   print(child.text)
   depth4 = child.find_element_by_class_name('hdline_article_tit')
   linkd[n] = depth4.find_element_by_tag_name('a').get_attribute('href')
   print(linkd[n])

   f=open('headline.txt','w+',encoding='utf-8')
   f.write(child.text)

   n=n+1

f.close()
browser.quit()

n=0
for n in range(len(linkd)):
   browser.get(linkd[n])
   time.sleep(5)
   fname='article'+str(n+1)+'.txt'
   news_tit=browser.find_element_by_id('articleTitle').text
   news_art=browser.find_element_by_id('articleBodyContents').text
   f=open(fname,'w',encoding='utf-8')
   f.write(news_tit)
   f.write(news_art)
   f.close()
   n=n+1

browser.quit()
