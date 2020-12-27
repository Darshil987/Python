import pymongo as pymo

myclient = pymo.MongoClient("mongodb://localhost:27017")

mydb = myclient['test']

mycol = mydb['customers']

list =[
    {"name": "Darshil", "EnNO": 170820107021 },
    {"name": "ABC", "EnNO": 1234 },
    {"name": "DEF", "EnNO": 5678 }
]
x = mycol.insert_many(list)

if x:
    print("Enter Successfully")
