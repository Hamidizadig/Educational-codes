from pymongo import MongoClient
from pprint import pprint, PrettyPrinter
client = MongoClient(host='localhost', port=27017)
# print(client)
dbTest = client['test']
# print(dbTest)
people = dbTest['People']
# print(people)
# # people.insert({'name':'misix','family':'shixakhes','age':19})
# print('_'*100)
# for db in client.list_database_names():
#     print(db)
# print('_'*100)
# for collection in dbTest.list_collection_names():
#     print(collection)
# print('_'*100)
# people.insert([
#                  {'name':'misix','family':'shixakhes','age':19},
#                  {'name':'mirash','family':'xplx','age':27}
#               ])
# for doc in people.find():
#     print(doc)

# for doc in people.find({'name':'istax'}):
#     print(doc)
# for doc in people.find({'name':'istax'}):
#     PrettyPrinter(indent=8,sort_dicts=False)
#     pprint(doc)

# print(people.find().count())

# people.update({'name':'misix'},{'$set':{'name':'misixius','family':'shixakhes','age':49}})
# for doc in people.find():
#     pprint(doc)


people.remove({'name': 'misix'})
for doc in people.find():
    pprint(doc)

client.close()
