from time import sleep

from youtubesearchpython import *
from selenium import webdriver

import json
from types import SimpleNamespace

DEBUG = False


def show_json_indentation(text):
    import json
    import re
    p = re.compile('(?<!\\\\)\'')
    text = p.sub('\"', text)
    parsed = json.loads(text)
    print(json.dumps(parsed, indent=4, sort_keys=True))


def play_music_with_bot_studio(url, title):
    from bot_studio.bot_studio import *
    bot_studio = bot_studio()
    youtube = bot_studio.youtube()
    youtube.open("http://www.youtube.com/watch?v=LMmuChXra_M")
    youtube.play_pause_video()
    bot_studio.send_feedback(feedback="Need help with this ......")


def play_music_with_webdriver(url, title):
    driver = webdriver.Firefox()
    driver.implicitly_wait(1)
    driver.maximize_window()
    driver.get(url)
    on_clicked = False
    trial = 3
    while on_clicked or trial > 0:
        try:
            print(f"on_clicked : {url}, {title}")
            driver.implicitly_wait(2)
            element = driver.find_element_by_partial_link_text(title)
            driver.implicitly_wait(1)
            element.click()
            on_clicked = True
        except Exception as e:
            print("try again!", e)
            trial -= 1


def open_url(url, title):
    print(f"open_url : {url}, {title}")
    play_music_with_webdriver(url, title)


def search_video(query):
    videos_search = VideosSearch(query, limit=10, language='en', region='US')
    text = str(videos_search.result(mode=ResultMode.json))
    if DEBUG: show_json_indentation(text)
    videos = json.loads(text, object_hook=lambda d: SimpleNamespace(**d))
    open_url(videos.result[0].link, videos.result[0].title)
