import json, pymongo


myclient = pymongo.MongoClient("mongodb://localhost:27017/",
                            connect=False)

MYDB = myclient['ballarpur']
VILLAGESCOLL = MYDB['villages_d']

colors = {'BJP': '#ff9933', 'INC': '#0000FF', 'VBA': '#FFC0CB', 'API': '#FFC0CB', 'IND': '#FFC0CB', 'BSP': '#FFC0CB', 'BSRP': '#FFC0CB', 'BMP': '#FFC0CB', 'PBI': '#FFC0CB', 'GGP': '#FFC0CB', 'SHS' : '#FFC0CB','RP(K)' : '#FFC0CB','MNS' : '#FFC0CB','NCP' : '#FFC0CB','CPI(M)' : '#FFC0CB','APOI' : '#FFC0CB','BMUP' : '#FFC0CB','RPI' : '#FFC0CB','SP(I)' : '#FFC0CB','LB' : '#FFC0CB','AITC' : '#FFC0CB','PRCP' : '#FFC0CB','OTHERS' : '#FFC0CB'}


file1 = open('abc3.json', "r")
file2 = open('final_abc3.json', "w")

data = json.loads(file1.read())
features = data['features']

new_features = []

for f in features:
    try:
        loc_id = f['properties']['loc_id']
        doc = VILLAGESCOLL.find_one({'location_id': str(loc_id)})
        win_2019 = doc['ls_2104']['votes_data'][0]['party']
        print(colors[win_2019])


        if win_2019 in colors:
          f['properties']['color'] = colors[win_2019]
        else:
          f['properties']['color'] = colors['OTHERS']



        new_features.append(f)

    except:
        new_features.append(f)
        pass
        
        


print(new_features)

data['features'] = new_features

file2.write(json.dumps(data))
