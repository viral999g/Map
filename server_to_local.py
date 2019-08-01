import json, pymongo


# MYCLIENT_SERVER = pymongo.MongoClient("mongodb://192.168.44.128:27017/",
#                             connect=False)

MYCLIENT_LOCAL = pymongo.MongoClient("mongodb://localhost:27017/",
                            connect=False)

# MYDB_SERVER = MYCLIENT_SERVER['ballarpur']
# VILLAGESCOLL_SERVER = MYDB_SERVER['villages_d']

MYDB_LOCAL = MYCLIENT_LOCAL['ballarpur']
VILLAGESCOLL_LOCAL = MYDB_LOCAL['villages_d']

file = open('data.json', 'w')
obj = {}

data = VILLAGESCOLL_LOCAL.find({}, {"_id": 0})
for d in data:
  obj[d['location_id']] = d

file.write(json.dumps(obj))