import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/",
                            connect=False)

MYDB = myclient['ballarpur']
VILLAGESCOLL = MYDB['villages_d']

data = VILLAGESCOLL.find()

# obj = {"कुणबी": [], "गोंड": [], "माळी": [], "तेली": [], "बौद्ध": []}
obj = {"कुणबी": [], "गोंड": [], "माळी": [], "तेली": [], "बौद्ध": []}

colors_obj = {"कुणबी": '#C0C0C0', "गोंड": '#808080', "माळी": '#FF0000', "तेली": '#F08080', "बौद्ध": '#FFA07A'}
white = '#FFFAF0'

for d in data:
  try:
    caste_data = d['caste_data']
    for c in caste_data:
      if c['caste'] in obj:
        c['location_id'] = d['location_id']
        obj[c['caste']].append(c)
  except:
    pass

for key, value in obj.items():
  obj[key].sort(key=lambda x: x['votes'], reverse=True)
# print(obj['कुणबी'])

for key, value in obj.items():
  obj[key] = value[0:15]

for key, value in obj.items():
  caste = key
  for v in value:
    VILLAGESCOLL.update({'location_id': v['location_id']}, {'$set': {key: colors_obj[key]}})


print(len(obj['कुणबी']))