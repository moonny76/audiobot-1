from sqlalchemy import or_

from mty_media_bot.database import DBManager
from mty_media_bot.model.music import Music


def sizeof_fmt(num):
    for x in ['bytes', 'KB', 'MB', 'GB']:
        if num < 1024.0:
            return "%3.1f%s" % (num, x)
        num /= 1024.0
    return "%3.1f%s" % (num, 'TB')


def search_music(search_word):
    if search_word == '':
        return get_all_music()

    music_list = DBManager.dao.query(Music). \
        filter(or_(Music.artist.like("%" + search_word + "%"),
                   Music.title.like("%" + search_word + "%"),
                   Music.filename.like("%" + search_word + "%"))). \
        order_by(Music.updated_date.desc()).all()

    return music_list


def get_all_music():
    return DBManager.dao.query(Music).order_by(Music.updated_date.desc()).all()
