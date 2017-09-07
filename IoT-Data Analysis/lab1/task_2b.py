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



	# Edit the query here
	results = coll.aggregate([{'$group': {'_id': '$temperature',
							   'avgTemperature': {'$avg': '$temperature'}}
	}]) 



	for doc in results:
		print(doc)

if __name__ == "__main__":
	main()
