import os

from tinytag import TinyTag

from mty_media_bot.assistant_logger import Log
from mty_media_bot.database import DBManager
from mty_media_bot.model.music import Music

ALLOWED_EXTENSIONS = {'mp3'}


def __allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def update_music(filename):
    try:
        if __allowed_file(filename):
            print(f'filename : {filename}')
            ext = filename.rsplit('.', 1)[1]
            filesize = os.stat(filename).st_size
            print(f'ext : {ext}')
            print(f'filesize : {filesize}')
            tag = TinyTag.get(filename)
            print(f'album : {tag.album}')
            print(f'artist : {tag.artist}')
            print(f'genre : {tag.genre}')
            print(f'title : {tag.title}')
        else:
            raise Exception("File update error : illegal file.")
    except Exception as e:
        Log.error(str(e))
        raise e

    try:
        music = Music(filename,
                      tag.title,
                      tag.artist,
                      tag.genre,
                      tag.album,
                      ext,
                      filesize)
        DBManager.dao.add(music)
        DBManager.dao.commit()

    except Exception as e:
        DBManager.dao.rollback()
        Log.error("Update DB error : " + str(e))
        raise e


def remove_music(id):
    try:
        music = DBManager.dao.query(Music).filter_by(id=id).first()

        DBManager.dao.delete(music)
        DBManager.dao.commit()

    except Exception as e:
        DBManager.dao.rollback()
        Log.error("Music remove error => " + id + ", " + str(e))
        raise e
