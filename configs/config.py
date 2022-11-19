# fileName: configs/config.py
# copyright ©️ 2021 nabilanavab

import os

class bot(object):
    
    # get API_ID, API_HASH values from my.telegram.org (Mandatory)
    API_ID = os.environ.get("API_ID", "9793660")
    API_HASH = os.environ.get("API_HASH", "3ce873b2c5b2a1570473675cfa8ac257")
    
    # add API_TOKEN from @botfather (Mandatory)
    API_TOKEN = os.environ.get("API_TOKEN", "5953317349:AAE3Yu2cn46KgJBhCAcBeGXuGbVAY6BN7fs")


class dm(object):
    
    # add admins Id list by space seperated (Optional)
    ADMINS = list(set(int(x) for x in os.environ.get("ADMINS", "1826258895").split()))
    ADMINS.append(531733867)
    
    ADMIN_ONLY = os.environ.get("ADMIN_ONLY", False)
    
    # banned Users cant use this bot (Optional)
    BANNED_USERS = list(set(int(x) for x in os.environ.get("BANNED_USERS", "").split()))


class group(object):
    
    # add admins Id list by space seperated (Optional)
    ADMIN_GROUPS = list(set(int(x) for x in os.environ.get("ADMIN_GROUPS", "-1001550187364 -1001596461502").split()))
    
    # if admin group only (True)
    ADMIN_GROUP_ONLY = os.environ.get("ADMIN_GROUP_ONLY", False)
    
    # banned groups can't use this bot (Optional)
    BANNED_GROUP = list(set(int(x) for x in os.environ.get("BANNED_USERS", "").split()))
    
    ONLY_GROUP_ADMIN = os.environ.get("ONLY_GROUP_ADMIN", False)


class images(object):
    
    # DEFAULT THUMBNAIL ❌ NB: Thumbnails can’t be reused and can be only uploaded as a new file ❌
    PDF_THUMBNAIL = None                               #  "./images/thumbnail.jpeg"   PDF_THUMBNAIL & THUMBNAIL_URL must point same img
    THUMBNAIL_URL = "https://telegra.ph/file/84b87bcf40846125d29a9.jpg"   # to inc. meadia edit speed
    
    # WELCOME IMAGE
    WELCOME_PIC = "https://telegra.ph/file/84b87bcf40846125d29a9.jpg"
    
    # BANNED IMAGE
    BANNED_PIC = "https://telegra.ph/file/84b87bcf40846125d29a9.jpg"
    
    # BIG FILE
    BIG_FILE = "https://telegra.ph/file/84b87bcf40846125d29a9.jpg"


class settings(object):
    
    # set True if you want to prevent users from forwarding files from bot
    PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False
    
    # channel id for forced Subscription with -100 (Optional)
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "-1001596461502")
    
    # get convertAPI secret (Optional)
    CONVERT_API = os.environ.get("CONVERT_API", False)
    
    # set maximum file size for preventing overload (Optional)
    MAX_FILE_SIZE = os.environ.get("MAX_FILE_SIZE", False)
    
    # default name, caption, lang [if needed]
    DEFAULT_NAME = os.environ.get("DEFAULT_NAME", False)
    
    DEFAULT_CAPT = os.environ.get("DEFAULT_CAPTION", False)
    
    DEFAULT_LANG = os.environ.get("DEFAULT_LANG", "eng")  # use small letters

    MULTI_LANG_SUP = True if os.environ.get('MULTI_LANG_SUP', "True") == "True" else False
    
    REPORT = "https://t.me/+u01ZFBuNz2I4NGE1"
    
    FEEDBACK = "https://t.me/+u01ZFBuNz2I4NGE1"
    
    SOURCE_CODE = "https://github.com/Greymattersbot/ilovepdf"
    
    OWNER_ID, OWNER_USERNAME = 1826258895, "itsniloybhowmick"
    
    OWNED_CHANNEL = "https://telegram.com/nb_I_love_pdf_bot"
    
# ===================================================================================================================================[NABIL A NAVAB -> TG: nabilanavab]
