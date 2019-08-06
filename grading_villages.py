import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/",
                            connect=False)

MYDB = myclient['ballarpur']
VILLAGESCOLL = MYDB['villages_d']

file = open("Location_Grading.csv", "r").readlines()

file.pop(0)

for line in file:
  columns = line.split(',')
  location = columns[0]
  grade = columns[1]

  VILLAGESCOLL.update({'location_id': location}, {'$set': {'grade': grade.replace("\n", "")}})