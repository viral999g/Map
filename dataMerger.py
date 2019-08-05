import pymongo, json, operator



# myclient = pymongo.MongoClient("mongodb://13.59.213.80:27017/",
#                             username='candles123',
#                             password='D1}d-0oMe[Ts8f>OPcjH,aiC',
#                             authSource='admin',
#                             connect=False)

myclient = pymongo.MongoClient("mongodb://localhost:27017/",
                            connect=False)

MYDB = myclient['ballarpur']
VILLAGESCOLL = MYDB['villages_d']

# file1 = open('Input/table1.csv', 'r').readlines()
# file2 = open('Input/table2.csv', 'r').readlines()
file3 = open('castedata2.csv', 'r').readlines()
# file4 = open('/media/viral999g/G/Projects/Map/Input/influencialpersons.csv', 'r').readlines()
# file5 = open('/media/viral999g/G/Projects/Map/Input/politicalpersons.csv', 'r').readlines()
# file7 = open('/media/viral999g/G/Projects/Map2/Map/2019.csv', 'r').readlines()
# file8 = open('/media/viral999g/G/Projects/Map/Input/vs_2014.csv', 'r').readlines()
# file9 = open('/media/viral999g/G/Projects/Map/Input/ls_2014.csv', 'r').readlines()
# file10 = open('/media/viral999g/G/Projects/Map/finalnames.csv', 'r').readlines()
# loc = '/media/viral999g/G/Projects/Map/Input/Issues.xlsx'

# wb = xlrd.open_workbook(loc) 
# sheet = wb.sheet_by_index(1) 
# file1.pop(0)
# file2.pop(0)
file3.pop(0)
# file4.pop(0)
# file5.pop(0)
# file10.pop(0)
# file10.pop(0)
# file10.pop(0)
# file10.pop(0)
# file10.pop(0)
# file7.pop(0)
# file6.pop(0)

data = {}
data2 = {}
data3 = {}
data4 = {}
data5 = {}
data6 = {}
data7 = {}
data8 = {}
data9 = {}

# for row in file1:
#     columns = row.split(',')
#     poll = columns[0]
#     location_id = columns[1]
#     taluka = columns[2].replace('\n', '')

#     if location_id in data:
#         data[location_id]['polling_booths'] += ", " + poll
#     else:
#         data[location_id] = {'polling_booths': poll, 'taluka': taluka}

# for row in file2:
#     columns = row.split(',')
#     location_id = columns[0]
#     name_hi = columns[1]

#     if location_id in data2:
#         pass
#     else:
#         data2[location_id] = {"name_hi" :name_hi.replace("\n", "")}        

for row in file3:
    columns = row.split(',')
    location_id = columns[0]
    caste_name = columns[3]

    voters = int(columns[6])

    # data3[location_id] = {caste_name : voters}

    if location_id in data3:
        data3[location_id][caste_name] = voters
    else:
        data3[location_id] = {caste_name : voters}

# for row in file4:
#     columns = row.split(',')
#     location_id = columns[0]

#     obj = {}
#     obj['pad'] = columns[2]
#     obj['first_name'] = columns[3]
#     obj['last_name'] = columns[4]
#     obj['caste'] = columns[5]
#     obj['age'] = columns[6]
#     obj['party'] = columns[7]
#     obj['mobile_no'] = columns[8].replace("\n", "")


#     if location_id in data4:
#         data4[location_id].append(obj)
#     else:
#         data4[location_id] = [obj]

# for row in file5:
#     columns = row.split(',')
#     location_id = columns[1]

#     obj = {}
#     obj['pad'] = columns[3]
#     obj['first_name'] = columns[4]
#     obj['last_name'] = columns[5]
#     obj['caste'] = columns[6]
#     obj['age'] = columns[7]
#     obj['party'] = columns[8]
#     obj['mobile_no'] = columns[9].replace("\n", "")


#     if location_id in data5:
#         data5[location_id].append(obj)
#     else:
#         data5[location_id] = [obj]

# rows = sheet.nrows
# print(int(sheet.cell_value(3,3)))

# for row in range(1, rows):
#     # print(sheet.cell_value(row, 2))
#     # print(row)
#     # columns = row.split(':')
#     location_id = int(sheet.cell_value(row, 3))
#     # print(file6.index(row))
#     # print(columns[2])
#     issue = sheet.cell_value(row, 2).replace("\xa0", "").replace("1.", "").strip()

#     if location_id in data6:
#         data6[location_id].append(issue)
#     else:
#         data6[location_id] = [issue] 
# candidates = file8.pop(0).split(",")
# parties = file8.pop(0).split(",")


# for row in file8:
#     columns = row.split(',')
#     location_id = columns[1]

#     obj = {}

#     votes_data = []
#     votes_data.append({"name": candidates[4], "party": parties[4], "votes": int(columns[4]), "votes_per": columns[5]})
#     votes_data.append({"name": candidates[6], "party": parties[6], "votes": int(columns[6]), "votes_per": columns[7]})
#     votes_data.append({"name": candidates[8], "party": parties[8], "votes": int(columns[8]), "votes_per": columns[9]})
#     votes_data.append({"name": candidates[10], "party": parties[10], "votes": int(columns[10]), "votes_per": columns[11]})
#     votes_data.append({"name": candidates[12], "party": parties[12], "votes": int(columns[12]), "votes_per": columns[13]})
#     votes_data.append({"name": candidates[14], "party": parties[14], "votes": int(columns[14]), "votes_per": columns[15]})
#     votes_data.append({"name": candidates[16], "party": parties[16], "votes": int(columns[16]), "votes_per": columns[17]})
#     votes_data.append({"name": candidates[18], "party": parties[18], "votes": int(columns[18]), "votes_per": columns[19]})
#     votes_data.append({"name": candidates[20], "party": parties[20], "votes": int(columns[20]), "votes_per": columns[21]})
#     votes_data.append({"name": candidates[22], "party": parties[22], "votes": int(columns[22]), "votes_per": columns[23]})
#     votes_data.append({"name": candidates[24], "party": parties[24], "votes": int(columns[24]), "votes_per": columns[25]})
#     votes_data.append({"name": candidates[26], "party": parties[26], "votes": int(columns[26]), "votes_per": columns[27]})
#     votes_data.append({"name": candidates[28], "party": parties[28], "votes": int(columns[28]), "votes_per": columns[29]})
#     votes_data.append({"name": candidates[30], "party": parties[30], "votes": int(columns[30]), "votes_per": columns[31]})
#     votes_data.append({"name": candidates[32], "party": parties[32], "votes": int(columns[32]), "votes_per": columns[33]})

#     obj['votes_data'] = sorted(votes_data ,key=lambda x: x['votes'], reverse=True)

#     obj['votes'] = columns[37]
    


#     data8[location_id] = obj

# parties = file7.pop(0).split(",")
# candidates = file7.pop(0).split(",")



# for row in file7:
#     columns = row.split(',')
#     location_id = columns[0]

#     obj = {}

#     votes_data = []
#     votes_data.append({"name": candidates[2], "party": parties[2], "votes": int(columns[2]), "votes_per": str(columns[3]).replace('.00', '')})
#     votes_data.append({"name": candidates[4], "party": parties[4], "votes": int(columns[4]), "votes_per": str(columns[5]).replace('.00', '')})
#     votes_data.append({"name": candidates[6], "party": parties[6], "votes": int(columns[6]), "votes_per": str(columns[7]).replace('.00', '')})
#     votes_data.append({"name": candidates[8], "party": parties[8], "votes": int(columns[8]), "votes_per": str(columns[9]).replace('.00', '')})
#     votes_data.append({"name": candidates[10], "party": parties[10], "votes": int(columns[10]), "votes_per": str(columns[11]).replace('.00', '')})
#     votes_data.append({"name": candidates[12], "party": parties[12], "votes": int(columns[12]), "votes_per": str(columns[13]).replace('.00', '')})
#     votes_data.append({"name": candidates[14], "party": parties[14], "votes": int(columns[14]), "votes_per": str(columns[15]).replace('.00', '')})
#     votes_data.append({"name": candidates[16], "party": parties[16], "votes": int(columns[16]), "votes_per": str(columns[17]).replace('.00', '')})
#     votes_data.append({"name": candidates[18], "party": parties[18], "votes": int(columns[18]), "votes_per": str(columns[19]).replace('.00', '')})
#     votes_data.append({"name": candidates[20], "party": parties[20], "votes": int(columns[20]), "votes_per": str(columns[21]).replace('.00', '')})
#     votes_data.append({"name": candidates[22], "party": parties[22], "votes": int(columns[22]), "votes_per": str(columns[23]).replace('.00', '')})
#     votes_data.append({"name": candidates[24], "party": parties[24], "votes": int(columns[24]), "votes_per": str(columns[25]).replace('.00', '')})
#     votes_data.append({"name": candidates[26], "party": parties[26], "votes": int(columns[26]), "votes_per": str(columns[27]).replace('.00', '')})


#     obj['votes_data'] = sorted(votes_data ,key=lambda x: x['votes'], reverse=True)

#     obj['votes'] = columns[31]
#     obj['electors'] = columns[33]
#     obj['turnout'] = columns[34]
    


#     data7[location_id] = obj







# candidates = file9.pop(0).split(",")
# parties = file9.pop(0).split(",")


# for row in file9:
#     columns = row.split(',')
#     location_id = columns[0]

#     obj = {}

#     votes_data = []
#     votes_data.append({"name": candidates[2], "party": parties[2], "votes": int(columns[2]), "votes_per": columns[3].replace(".00", "")})
#     votes_data.append({"name": candidates[4], "party": parties[4], "votes": int(columns[4]), "votes_per": columns[5].replace(".00", "")})
#     votes_data.append({"name": candidates[6], "party": parties[6], "votes": int(columns[6]), "votes_per": columns[7].replace(".00", "")})
#     votes_data.append({"name": candidates[8], "party": parties[8], "votes": int(columns[8]), "votes_per": columns[9].replace(".00", "")})
#     votes_data.append({"name": candidates[10], "party": parties[10], "votes": int(columns[10]), "votes_per": columns[11].replace(".00", "")})
#     votes_data.append({"name": candidates[12], "party": parties[12], "votes": int(columns[12]), "votes_per": columns[13].replace(".00", "")})
#     votes_data.append({"name": candidates[14], "party": parties[14], "votes": int(columns[14]), "votes_per": columns[15].replace(".00", "")})
#     votes_data.append({"name": candidates[16], "party": parties[16], "votes": int(columns[16]), "votes_per": columns[17].replace(".00", "")})
#     votes_data.append({"name": candidates[18], "party": parties[18], "votes": int(columns[18]), "votes_per": columns[19].replace(".00", "")})
#     votes_data.append({"name": candidates[20], "party": parties[20], "votes": int(columns[20]), "votes_per": columns[21].replace(".00", "")})
#     votes_data.append({"name": candidates[22], "party": parties[22], "votes": int(columns[22]), "votes_per": columns[23].replace(".00", "")})
#     votes_data.append({"name": candidates[24], "party": parties[24], "votes": int(columns[24]), "votes_per": columns[25].replace(".00", "")})
#     votes_data.append({"name": candidates[26], "party": parties[26], "votes": int(columns[26]), "votes_per": columns[27].replace(".00", "")})
#     votes_data.append({"name": candidates[28], "party": parties[28], "votes": int(columns[28]), "votes_per": columns[29].replace(".00", "")})
#     votes_data.append({"name": candidates[30], "party": parties[30], "votes": int(columns[30]), "votes_per": columns[31].replace(".00", "")})
#     votes_data.append({"name": candidates[32], "party": parties[32], "votes": int(columns[32]), "votes_per": columns[33].replace(".00", "")})
#     votes_data.append({"name": candidates[34], "party": parties[32], "votes": int(columns[34]), "votes_per": columns[35].replace(".00", "")})
#     votes_data.append({"name": candidates[36], "party": parties[32], "votes": int(columns[36]), "votes_per": columns[37].replace(".00", "")})

#     obj['votes_data'] = sorted(votes_data ,key=lambda x: x['votes'], reverse=True)

#     obj['votes'] = columns[41]
    


#     data9[location_id] = obj




# print(data['1'])

# print(len(data2))

# for d, v in data2.items():
#     VILLAGESCOLL.update({'location_id': d}, {"$set": {"name_hi": v['name_hi']}})

for k, v in data3.items():
    caste_data = []
    for d in sorted(data3[k].items(), key = operator.itemgetter(1), reverse=True):
        caste_data.append({'caste': d[0].replace("\n",""), 'votes': d[1]})

    VILLAGESCOLL.update({'location_id': k}, {"$set": {"caste_data": caste_data}})
    


# for d, v in data5.items():
#     VILLAGESCOLL.update({'location_id': d}, {"$set": {"politicalal_persons": v}})

# for d, v in data6.items():
#     VILLAGESCOLL.update({'location_id': str(d)}, {"$set": {"issues": v}})


# print(data7)

# for d, v in data7.items():
#     VILLAGESCOLL.update({'location_id': str(d)}, {"$set": {"election_2019": v}})

# for d, v in data8.items():
#     VILLAGESCOLL.update({'location_id': str(d)}, {"$set": {"vs_2014": v}})

# for d, v in data9.items():
#     VILLAGESCOLL.update({'location_id': str(d)}, {"$set": {"ls_2014": v}})

# for row in file10:
#     columns = row.split(",")
#     location_id = columns[2]
#     name_en = columns[1]

#     VILLAGESCOLL.update({'location_id': location_id}, {"$set": {'name_en': name_en}})