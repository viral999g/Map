import json, pymongo


myclient = pymongo.MongoClient("mongodb://13.59.213.80:27017/",
                            username='candles123',
                            password='D1}d-0oMe[Ts8f>OPcjH,aiC',
                            authSource='admin',
                            connect=False)

MYDB = myclient['ballarpur']
VILLAGESCOLL = MYDB['villages_d']


file1 = open('abc1.json', "r")
file2 = open('final_abc1.json', "w")

data = json.loads(file1.read())
features = data['features']

new_features = []

for f in features:
    try:
        f['properties']['loc_id'] = f['properties']['loc id']
        name = VILLAGESCOLL.find_one({'location_id': str(f['properties']['loc id'])})['name_en']
        print(name)

        f['properties']['name_en'] = name


        new_features.append(f)

    except:
        new_features.append(f)
        


print(new_features)

data['features'] = new_features

file2.write(json.dumps(data))
