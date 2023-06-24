import pymongo

client = pymongo.MongoClient()

mydb = client["mydb"]

myCollection = mydb["people"]

data = {'name':'john honay', 'age':28}

x = myCollection.insert_one(data)

print(x.inserted_id)

dataList = [{'name':'Mark', 'age':45}, {'name':'Mark', 'age':25}]

y = myCollection.insert_many(dataList)

print(y.inserted_ids)