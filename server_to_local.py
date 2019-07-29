import json, pymongo


MYCLIENT_SERVER = pymongo.MongoClient("mongodb://13.59.213.80:27017/",
                            username='candles123',
                            password='D1}d-0oMe[Ts8f>OPcjH,aiC',
                            authSource='admin',
                            connect=False)

MYCLIENT_LOCAL = pymongo.MongoClient("mongodb://localhost:27017/",
                            connect=False)

MYDB_SERVER = MYCLIENT_SERVER['ballarpur']
VILLAGESCOLL_SERVER = MYDB_SERVER['villages_d']

MYDB_LOCAL = MYCLIENT_LOCAL['ballarpur']
VILLAGESCOLL_LOCAL = MYDB_LOCAL['villages_d']

data = VILLAGESCOLL_SERVER.find()
for d in data:
  VILLAGESCOLL_LOCAL.insert(d)