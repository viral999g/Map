import json, pymongo


myclient = pymongo.MongoClient("mongodb://localhost:27017/",
                            username='candles123',
                            password='D1}d-0oMe[Ts8f>OPcjH,aiC',
                            authSource='admin',
                            connect=False)

# myclient = pymongo.MongoClient("mongodb://localhost:27017/",
#                             connect=False)

MYDB = myclient['ballarpur']
VILLAGESCOLL = MYDB['villages_d']

data = VILLAGESCOLL.find()

print(data.count())

for d in data:
  try:
    caste_data = d['caste_data']
    for r in caste_data:
      if r['caste'] == '#N/A':
        caste_data.pop(caste_data.index(r))

    VILLAGESCOLL.update({'location_id': d['location_id']}, {"$set": {'caste_data': caste_data}})
  except:
    print("Error")

