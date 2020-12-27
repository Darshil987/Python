import pymongo as pymo

myclient = pymo.MongoClient("mongodb://localhost:27017")

mydb = myclient['test']

mycol = mydb['customers']

myquery = {"name": {"$regex": "^D"}}
new = {"$set": {"EnNO": 152}}

mycol.update_many(myquery, new)

for x in mycol.find():
    print(x)
