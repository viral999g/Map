import json, pymongo


myclient = pymongo.MongoClient("mongodb://13.59.213.80:27017/",
                            username='candles123',
                            password='D1}d-0oMe[Ts8f>OPcjH,aiC',
                            authSource='admin',
                            connect=False)

MYDB = myclient['ballarpur']
VILLAGESCOLL = MYDB['villages_d']


file1 = open('abc1.json', "r")
file2 = open('abc2.json', "w")

data = json.loads(file1.read())
features = data['features']

new_features = []

for f in features:
    try:
        if f['properties']['loc_id'] == None:
            f['properties']['color'] = '#008000'

        new_features.append(f)

    except:
        new_features.append(f)
        


print(new_features)

data['features'] = new_features

file2.write(json.dumps(data))
