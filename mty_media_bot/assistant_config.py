class Config(object):
    #: 데이터베이스 연결 URL
    DB_URL= 'sqlite:///'
    #: 데이터베이스 파일 경로
    DB_FILE_PATH= 'resource/database/assistant.db'
    #: 로그 레벨 설정
    LOG_LEVEL = 'debug'
    #: 디폴트 로그 파일 경로
    LOG_FILE_PATH = 'resource/log/assistant.log'
    #: 디폴트 SQLAlchemy trace log 설정
    DB_LOG_FLAG = 'True'
