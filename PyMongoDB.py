import pymongo as pymo

myclient = pymo.MongoClient("mongodb://localhost:27017")

mydb = myclient['test']

mycol = mydb['customers']

myquery = {"Country": "dcsdf"}
new = {"$set": {"Country": "India"}}

mycol.update_one(myquery, new)

for x in mycol.find():
    print(x)
