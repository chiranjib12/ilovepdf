# fileName: configs/db.py
# copyright ©️ 2021 nabilanavab

import os

 # if os.environ.get("MONGODB_URI", False):
 #    from database import db
DATA = {}                                                                    # save user api, fname, capt
                                                                             # if UPDATE_CHANNEL
invite_link = []                                                             # just saves invitation link

BANNED_USR_DB, BANNED_GRP_DB = [], []                                        # Load Banned Users Id

CUSTOM_THUMBNAIL_U, CUSTOM_THUMBNAIL_C = [], []                              # Load UsersId with custom thumbnail

class dataBASE(object):
    
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://ilovepdf:ilovepdf@ilovepdf.e28ohab.mongodb.net/?retryWrites=true&w=majority")                       # mongoDB Url (Optional)

                                                                             # Telegram: @nabilanavab
