from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from mty_media_bot.model import Base


class Music(Base):
    __tablename__ = 'musics'

    id = Column(Integer, primary_key=True)
    filename = Column(String(100), unique=False)
    title = Column(String(200), unique=False)
    artist = Column(String(50), unique=False)
    genre = Column(String(20), unique=False)
    album = Column(String(100), unique=False)
    ext = Column(String(10), unique=False)
    filesize = Column(Integer, unique=False)
    updated_date = Column(DateTime, unique=False)

    def __init__(self, filename, title, artist, genre, album, ext, filesize):
        self.filename = filename
        self.title = title
        self.artist = artist
        self.genre = genre
        self.album = album
        self.ext = ext
        self.filesize = filesize
        self.updated_date = datetime.now()

    def __repr__(self):
        return '<Music %r %r>' % (self.filename, self.updated_date)
