import pymongo as pymo

myclient = pymo.MongoClient("mongodb://localhost:27017")

mydb = myclient['test']

mycol = mydb['customers']

myquery = {"EnNO": 170820107021}
for x in mycol.find(myquery):
    print(x)

