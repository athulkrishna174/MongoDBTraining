import pymongo

client = pymongo.MongoClient()

mydb = client["mydb"]

myCollection = mydb["customers"]

for x in myCollection.find({'address': { "$regex": "^O" }}, {'_id':0, 'name':1, 'address':1}).sort('name', -1):  # $regex for regular expression
    print(x)