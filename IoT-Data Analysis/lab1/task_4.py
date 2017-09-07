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
	results = coll.aggregate([{
		'$match' : {'$and': [
								{'created_at': {'$gte' : datetime.datetime(2017, 8, 24, 0, 0, 0)}},
								{'created_at': {'$lte' : datetime.datetime(2017, 8, 24, 23, 59, 59)}}
							]
					}
	}, {
		'$group': {'_id' : None, 'maxTemperature' :  {'$max': '$temperature'},
				   'minTemperature' : {'$min': '$temperature'}, 'avgTemperature' : {'$avg': '$temperature'}}
	}]) 




	for doc in results:
		print('A temperature of %2.3fºC was detected by %s.' % (doc['temperature'], doc['created_at'].strftime('%H:%M:%S')))

if __name__ == "__main__":
	main()
