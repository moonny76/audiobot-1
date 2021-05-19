import os
from mty_media_bot.assistant_config import Config
from mty_media_bot.service.parser_music import update_database


def create_app():
    # 로그 초기화
    root = "."
    from mty_media_bot.assistant_logger import Log
    log_filepath = os.path.join(root, Config.LOG_FILE_PATH)
    Log.init(log_filepath=log_filepath)

    # 데이터베이스 처리
    from mty_media_bot.database import DBManager
    db_filepath = os.path.join(root,
                               Config.DB_FILE_PATH)
    db_url = Config.DB_URL + db_filepath
    DBManager.init(db_url, eval(Config.DB_LOG_FLAG))
    DBManager.init_db()
    update_database()
