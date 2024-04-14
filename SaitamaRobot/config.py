import json
import os


def get_user_list(config, key):
    with open('{}/SaitamaRobot/{}'.format(os.getcwd(), config),
              'r') as json_file:
        return json.load(json_file)[key]


class Config(object):
    LOGGER = True
    
    API_ID = 123456  
    API_HASH = "awoo"
    TOKEN = "BOT_TOKEN"  
    OWNER_ID = 792109647  
    OWNER_USERNAME = "Sawada"
    SUPPORT_CHAT = 'OnePunchSupport'  
    JOIN_LOGGER = -1001253661229  
    EVENT_LOGS = -1001190806654 

 
    SQLALCHEMY_DATABASE_URI = 'something://somewhat:user@hosturl:port/databasename'  
    LOAD = []
    NO_LOAD = ['rss', 'cleaner', 'connection', 'math']
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = ""  
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    
    DRAGONS = get_user_list('elevated_users.json', 'sudos')
    
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
    BAN_STICKER = ''  
    ALLOW_EXCL = True  
    CASH_API_KEY = 'awoo'  
    TIME_API_KEY = 'awoo'  
    WALL_API = 'awoo'  
    AI_API_KEY = 'awoo'  
    BL_CHATS = []  
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
