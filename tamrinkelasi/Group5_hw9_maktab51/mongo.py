from pymongo import MongoClient
import json

client = MongoClient('localhost', 27017)
db = client.test
inventory = db.inventory
print(inventory.find_one())

# with open('data.json') as info:
#     read = json.load(info)
# inventory.insert_many(read)

data = [
    {
        "person_id": "6392529400",
        "firstname": "Elise",
        "lastname": "Smith",
        "vocation": "ENGINEER",
        "address": {
            "number": 5625,
            "street": "Tipa Circle",
            "city": "Wojzinmoj",
        },
    },
    {
        "person_id": "1723338115",
        "firstname": "Olive",
        "lastname": "Ranieri",
        "gender": "FEMALE",
        "vocation": "ENGINEER",
        "address": {
            "number": 9303,
            "street": "Mele Circle",
            "city": "Tobihbo",
        },
    },
    {
        "person_id": "8732762874",
        "firstname": "Toni",
        "lastname": "Jones",
        "vocation": "POLITICIAN",
        "address": {
            "number": 1,
            "street": "High Street",
            "city": "Upper Abbeywoodington",
        },
    }, {
        "person_id": "7363629563",
        "firstname": "Bert",
        "lastname": "Gooding",
        "vocation": "FLORIST",
        "address": {
            "number": 13,
            "street": "Upper Bold Road",
            "city": "Redringtonville",
        },
    },
]
db.people.insert_many(data)

data2 = [
    {
        "person_id": "1029648329",
        "firstname": "Sophie",
        "lastname": "Celements",
        "vocation": "ENGINEER",
        "address": {
            "number": 5,
            "street": "Innings Close",
            "city": "Basilbridge",
        },
    },
    {
        "person_id": "7363626383",
        "firstname": "Carl",
        "lastname": "Simmons",
        "vocation": "ENGINEER",
        "address": {
            "number": 187,
            "street": "Hillside Road",
            "city": "Kenningford",
        },
    }]
db.people.insert_many(data2)
a = db.people.count()
print(a)

db.people.aggregate([{'$match': {'vocation': 'ENGINEER'}},
                     {'$group': {'_id': '$address.city', 'total': {'$sum': 1}}}
                     ])
