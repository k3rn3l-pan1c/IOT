from pymongo import MongoClient
import datetime
import time
import sys

__author__ = "Diogo Regateiro"
__email__ = "diogoregateiro@ua.pt"
__version__ = "1.0"

def main():
	# Get the client, database and collection
	client = MongoClient('193.136.92.104')
	db = client['bestiot']
	coll = db['weather']



	# Leave only one uncommented query to run the script
	
	results = coll.find().limit(5) 

#	results = coll.find({'temperature': 25.5}) 

#	results = coll.aggregate([{
#		'$match': { 'temperature': { '$gte': 25.5 } }
#	}]) 

#	results = coll.aggregate([{
#		'$match': {'temperature': {'$gte': 25.5}}
#	}, {
#		'$group': {'_id': '$temperature', 'avgHumidity': {'$avg': '$humidity'}}
#	}])

#	results = coll.aggregate([{
#		'$group': {'_id': None, 'avgHumidity': {'$avg': '$humidity'}}
#	}])

#	results = coll.aggregate([{ 
#		'$match': { '$and': [
#			{ 'created_at': {'$gte' : datetime.datetime(2017,8,24,9)} }, 
#			{ 'created_at': {'$lte' : datetime.datetime(2017,8,24,10)} }
#		]}
#	}])



	for doc in results:
		print(doc)	

if __name__ == "__main__":
	main()
