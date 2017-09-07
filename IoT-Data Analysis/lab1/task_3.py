from pymongo import MongoClient
import datetime
import json
import time
import sys

__author__ = "Diogo Regateiro"
__email__ = "diogoregateiro@ua.pt"
__version__ = "1.0"

def main():
	# Get the client, database and collection
	client = MongoClient('193.136.92.104')
	db = client['bestiot']
	coll = db['bench']
	
	entry = {
		'entry_id': -1,
		'temperature': 1.0, 
		'humidity': 2.0,
		'pressure': 3.0,
		'dew_point': 4.0,
		'heat_index': 5.0,
		'altitude': 6.0,
		'rssi': 7.0,
		'created_at': datetime.datetime.now()
	}

	# Measure Insertion
	elapsed = time.time()
	result = coll.insert_one(entry)
	elapsed = time.time() - elapsed
	print('Insertion took %f seconds.' % (elapsed))

	# Measure Update
	elapsed = time.time()
	coll.update_one({"_id": result.inserted_id}, {"$set": { "temperature": 25.0 }}, upsert=False)
	elapsed = time.time() - elapsed
	print('Update took %f seconds.' % (elapsed))

	coll.delete_many({"_id": result.inserted_id})
	
if __name__ == "__main__":
	main()
