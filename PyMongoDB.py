import pymongo as pymo

myclient = pymo.MongoClient("mongodb://localhost:27017")

mydb = myclient['test']

mycol = mydb['customers']

for x in mycol.find().sort("EnNO", -1):
    print(x)

