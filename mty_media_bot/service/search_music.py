import time

from sqlalchemy import or_

from mty_media_bot.database import DBManager
from mty_media_bot.model.music import Music


def sizeof_fmt(num):
    for x in ['bytes', 'KB', 'MB', 'GB']:
        if num < 1024.0:
            return "%3.1f%s" % (num, x)
        num /= 1024.0
    return "%3.1f%s" % (num, 'TB')


def search_music_by_filename(filename):
    return DBManager.dao.query(Music).filter(Music.filename==filename)


def search_music(search_word):
    if search_word == '':
        return get_all_music()
    keyword = search_word.split()[0]
    music_list = DBManager.dao.query(Music). \
        filter(or_(Music.artist.like("%" + keyword + "%"),
                   Music.title.like("%" + keyword + "%"),
                   Music.filename.like("%" + keyword + "%"))). \
        order_by(Music.updated_date.desc()).all()

    if len(music_list) == 0:
        return
    from audioplayer import AudioPlayer
    player = AudioPlayer(music_list[0].filename)
    player.play()
    time.sleep(10)
    player.close()


    return music_list


def get_all_music():
    return DBManager.dao.query(Music).order_by(Music.updated_date.desc()).all()
