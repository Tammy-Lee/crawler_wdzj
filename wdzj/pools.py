# -*- coding: utf-8 -*-
"""
create on 2018-08-19 17:01
author @66492
"""

import pymongo
from wdzj import config

_client = pymongo.MongoClient(config.MONGO_URL)
mongo_db = _client[config.MONGO_DB_NAME]
if config.MONGO_AUTH:
    mongo_db.authenticate(**config.MONGO_AUTH)
