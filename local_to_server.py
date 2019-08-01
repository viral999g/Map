import json, pymongo



MYCLIENT_LOCAL = pymongo.MongoClient("mongodb://localhost:27017/",
                            connect=False)

MYDB_LOCAL = MYCLIENT_LOCAL['ballarpur']
VILLAGESCOLL_LOCAL = MYDB_LOCAL['villages_d']

file = open('data.json', 'r')

data = json.loads(file.read())
for d, v in data.items():
  VILLAGESCOLL_LOCAL.insert(v)

