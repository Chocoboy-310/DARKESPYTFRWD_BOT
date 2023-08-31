import os

class Config(object):
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6565969208:AAEeJI6JE_d4bTYANvDDHXQ7U0t4uRTRrcc")

    APP_ID = int(os.environ.get("APP_ID", 21814194))

    API_HASH = os.environ.get("API_HASH", "9535a6cee1e1d8e3a97a245f73b2d52a")    
    
    CAPTION_TEXT = os.environ.get("CAPTION_TEXT", "Join For More :\n @DARKESPYT")

    CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "bottom")

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
