import random
from pymongo import MongoClient

# connection = MongoClient('hostname')
connection = MongoClient()
# db = connection.admin
# db.authenticate('username','password')

db = connection['pd5']
print db.collection_names()

names = ["Winton","Steve","Arvindonshal"]

dtype = ['plain','frosted']

for l in range(10):
    d = {'name':random.choice(names),
         'dtype':random.choice(dtype)}
    print d
    db.insert(d)

res = db.pd5.find('donut':'plain')
print res
