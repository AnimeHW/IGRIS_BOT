import json
import os


def get_user_list(config, key):
    with open('{}/SaitamaRobot/{}'.format(os.getcwd(), config),
              'r') as json_file:
        return json.load(json_file)[key]


class Config(object):
    LOGGER = True
    
    API_ID = 21732614  
    API_HASH = "ff91cccbb310e68d0b93320abb2d229d"
    TOKEN = "6563345274:AAH7LT6Mqc3_ZoMiJgA-ox_s8zf_73MCxQ0"  
    OWNER_ID = 6710268098  
    OWNER_USERNAME = "Shadizinho"
    SUPPORT_CHAT = 'IGRISSx_sup'  
    JOIN_LOGGER = -1002069292433  
    EVENT_LOGS = -1001984580263 

 
    SQLALCHEMY_DATABASE_URI = 'mongodb+srv://Igris:Ggae4304,,@igris.oxdjuul.mongodb.net/'  
    LOAD = []
    NO_LOAD = ['rss', 'cleaner', 'connection', 'math']
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "ltwfo4Z7BG3tF4vQn~sWauW6q06ZpICxEtueM09l5yceJKkR4uxPV2O8PbwY1IEs"  
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    
    DRAGONS = get_user_list('7080925947', '6959003848')
    
    DEV_USERS = get_user_list('elevated_users.json', 'devs')
    
    DEMONS = get_user_list('elevated_users.json', 'supports')
    
    TIGERS = get_user_list('elevated_users.json', 'tigers')
    WOLVES = get_user_list('elevated_users.json', 'whitelists')
    DONATION_LINK = None  
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  
    STRICT_GBAN = True
    WORKERS = 8  
    BAN_STICKER = 'CAACAgQAAxkBAAEXXIpmGojxnkWCeFAtfDs2w2ggbkOf6wACdRMAAue1kFOMHaxTFlb8_TQE'  
    ALLOW_EXCL = True  
    CASH_API_KEY = 'XDG2I0AAURMP8QXI'  
    TIME_API_KEY = 'KNJIWN8SZBVX'  
    WALL_API = 'https://api.alphacoders.com/3.0?type=desktop&method=wallpaper_info&id=865098'  
    AI_API_KEY = 'AIzaSyAyNlhxI4q-fcFEH2eYUjU9xc9fYZ5Q66s'  
    BL_CHATS = []  
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
