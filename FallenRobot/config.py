import os

class Config(object):
    LOGGER = bool(os.environ.get("LOGGER", True))

    API_ID = int(os.environ.get("API_ID", 6))
    API_HASH = os.environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
    
    CASH_API_KEY = os.environ.get("CASH_API_KEY", "")
    DATABASE_URL = os.environ.get("DATABASE_URL", "")
    EVENT_LOGS = os.environ.get("EVENT_LOGS", ())
    MONGO_DB_URI = os.environ.get("MONGO_DB_URI", "")
    
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/40eb1ed850cdea274693e.jpg")
    
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "DevilsHeavenMF")
    TOKEN = os.environ.get("TOKEN", "")
    TIME_API_KEY = os.environ.get("TIME_API_KEY", "")
    
    OWNER_ID = int(os.environ.get("OWNER_ID", 1356469075))

    # For lists, assuming comma-separated values in the environment variable
    BL_CHATS = os.environ.get("BL_CHATS", "").split(',')
    DRAGONS = os.environ.get("DRAGONS", "").split(',')
    DEV_USERS = os.environ.get("DEV_USERS", "").split(',')
    DEMONS = os.environ.get("DEMONS", "").split(',')
    TIGERS = os.environ.get("TIGERS", "").split(',')
    WOLVES = os.environ.get("WOLVES", "").split(',')

    ALLOW_CHATS = bool(os.environ.get("ALLOW_CHATS", True))
    ALLOW_EXCL = bool(os.environ.get("ALLOW_EXCL", True))
    DEL_CMDS = bool(os.environ.get("DEL_CMDS", True))
    INFOPIC = bool(os.environ.get("INFOPIC", True))
    LOAD = os.environ.get("LOAD", "").split(',')
    NO_LOAD = os.environ.get("NO_LOAD", "").split(',')
    STRICT_GBAN = bool(os.environ.get("STRICT_GBAN", True))
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./")
    WORKERS = int(os.environ.get("WORKERS", 8))

class Production(Config):
    LOGGER = bool(os.environ.get("PRODUCTION_LOGGER", True))

class Development(Config):
    LOGGER = bool(os.environ.get("DEVELOPMENT_LOGGER", True))

