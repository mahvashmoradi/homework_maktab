from pymongo import MongoClient
import json

client = MongoClient('localhost', 27017)
db = client.hw8_data
inventory = db.inventory
#print(inventory.find_one())

with open('G:\maktab\homework\Maktab51-HW8\Maktab51-HW8\data.json') as info:
    read = json.load(info)
inventory.insert_many(read)
#inventory.delete_many({})

a = db.inventory.count()
print(a)
