import pymongo as pymo

myclient = pymo.MongoClient("mongodb://localhost:27017")

mydb = myclient['test']

mycol = mydb['customers']

list =[
    {"_id": 1, "name": "Darshil", "EnNO": 170820107021 },
    {"_id": 2, "name": "ABC", "EnNO": 1234 },
    {"_id": 3, "name": "DEF", "EnNO": 5678 }
]
x = mycol.insert_many(list)

if x:
    print("Enter Successfully")
    print(x.inserted_ids)
