import json, pymongo


myclient = pymongo.MongoClient("mongodb://localhost:27017/",
                            connect=False)

MYDB = myclient['ballarpur']
VILLAGESCOLL = MYDB['villages_d']

colors = {'BJP': '#ff9933', 'INC': '#0000FF', 'VBA': '#FFC0CB', 'API': '#FFC0CB', 'IND': '#FFC0CB', 'BSP': '#FFC0CB', 'BSRP': '#FFC0CB', 'BMP': '#FFC0CB', 'PBI': '#FFC0CB', 'GGP': '#FFC0CB', 'SHS' : '#FFC0CB','RP(K)' : '#FFC0CB','MNS' : '#FFC0CB','NCP' : '#FFC0CB','CPI(M)' : '#FFC0CB','APOI' : '#FFC0CB','BMUP' : '#FFC0CB','RPI' : '#FFC0CB','SP(I)' : '#FFC0CB','LB' : '#FFC0CB','AITC' : '#FFC0CB','PRCP' : '#FFC0CB','OTHERS' : '#FFC0CB'}
# colors_obj = {"A": '#F05E23', "B": '#0000ff', "B+": '#fda50f', "C": '#7CFC00', "others": "#FFFAF0"}
colors_obj = {"कुणबी": '#FF0000', "गोंड": '#0000FF', "माळी": '#ff9933', "तेली": '#556b2f', "बौद्ध": "#00eeee", "others": "#FFFAF0"}


file1 = open('final_abc1.json', "r")
file2 = open('cat.json', "w")

data = json.loads(file1.read())
features = data['features']


villages = []
color_data = VILLAGESCOLL.find()
for c in color_data:
  villages.append(c['location_id'])

print(villages)

new_features = []

sett = set()

for f in features:
    try:
      loc_id = str(f['properties']['loc_id'])
      # doc = VILLAGESCOLL.find_one({'location_id': str(loc_id)})
      # win_2019 = doc['ls_2104']['votes_data'][0]['party']
      # print(colors[win_2019])


      # if win_2019 in colors:
      #   f['properties']['color'] = colors[win_2019]
      # else:
      #   f['properties']['color'] = colors['OTHERS']
      # print(type(loc_id))

      # if loc_id in villages:
      #   print("yes")
      
      # if loc_id in villages:
      #   sett.add(loc_id)

      doc = VILLAGESCOLL.find_one({"location_id": loc_id})
      grade = doc['grade']


      f['properties']['color'] = colors_obj[grade]
      new_features.append(f)

    except:
        f['properties']['color'] = colors_obj['others']

        new_features.append(f)
        pass
        
        


print(sett)

data['features'] = new_features

file2.write(json.dumps(data))
