# coding: utf-8

from pymongo import MongoClient
import numpy as np
from datetime import datetime, timedelta
from sklearn import preprocessing
from sklearn import linear_model
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import LinearSVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt


__author__ = "Mário Antunes"
__email__ = "mario.antunes@ua.pt"
__version__ = "1.0"

# Given a dataset it returns an roll version.
# The roll version is used in time series prediction.
# roll parameter controls how much past should be included in the prediction
def roll_dataset(dataset, roll=2):
    # Task 3: For each day, add the previous N (roll) days information to it.
    rdataset=[]

    for i in range(0, len(dataset) - roll):
        rdataset.append([])
        for k in range(0, roll-1):
            rdataset[i].extend(dataset[i] + dataset[i + k])

    return np.array(rdataset)

# Loads a dataset from a mongodb instance.
# Uses a whole day has a input.
def load_dataset():
    # Get the client, database and collection
    client = MongoClient('193.136.92.104')
    db = client['bestiot']
    coll = db['weather']
    dataset = []

    # Retrieve data and make a summary
    # Task 2: Add more days to create more summaries
    days = [(8, i) for i in range(1,31)]
    print(days)
    for d in days:#[(8, 18), (8, 19), (8,20), (8,21), (8,22), (8,23), (8,24), (8,25), (8,26)]:
        row = []

	# Task 4: Divide the day further into blocks (mind the start and end time)
        for h in [0]:
            start = datetime(2017, d[0], d[1], h)
            end = start + timedelta(hours=24)

            # Task 1: Write your query here
            result = coll.aggregate([{
            '$group' : { '_id' : None,
                         'avgTemp' : {'$avg': '$temperature'}, 'minTemp' : {'$min': '$temperature'}, 'maxTemp' : {'$max': '$temperature'},
                         'avgHum' : {'$avg': '$humidity'}, 'minHum' : {'$min': '$humidity'}, 'maxHum' : {'$max': '$humidity'},
                         'avgPressure' : {'$avg': '$pressure'}, 'minPressure' : {'$min': '$pressure'}, 'maxPressure' : {'$max': '$pressure'},
                       }
            }])

            rv = list(result)[0]

            # Task 1: Add your aggregated fields here, eg. row.extend([rv['minTemp'], rv['maxTemp']])
            row.extend([rv['avgTemp'], rv['minTemp'], rv['maxTemp'], rv['avgHum'], rv['minHum'], rv['maxHum'], rv['avgPressure'], rv['minPressure'], rv['maxPressure']])

        start = datetime(2017, d[0], d[1])
        end = start + timedelta(hours=24)

	# The precipitation data should always be the last column in the row
        rv = coll.find_one({'$and': [{'precipitation': {'$exists': True}},{'created_at': {'$gte': start}},
                                     {'created_at': {'$lte': end}}]})
        row.append(rv['precipitation'])
        dataset.append(row)
    client.close()
    return np.array(dataset)


def main():
    print('Predicting precipitation based on sensory data.\n')
    dataset = load_dataset()
    print('Dataset:\n')
    print(dataset)
    rdataset = roll_dataset(dataset)

    scaler = preprocessing.MinMaxScaler()

    # Divide dataset into input(X) and output(Y)
    # Normalize input features (pressure two orders of magnitude higher than the other)
    X = scaler.fit_transform(rdataset[:, :rdataset.shape[1]-2])
    y = rdataset[:, rdataset.shape[1]-1].reshape(-1, 1)
    #print(X)
    #print(Y)

    # Split the dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle=False, stratify=None)

    #print(X_test)
    #print(y_test)

    model_names = ['linear regression', 'decision tree', 'k nearest neighbors', 'svm']
    models = [linear_model.LinearRegression(), DecisionTreeRegressor(max_depth=2),
              KNeighborsRegressor(n_neighbors=min(len(X_test), 3), weights='distance'), LinearSVR()]

    plots = []

    # Test several models to evaluate performance
    for i in range(0, len(models)):
        models[i].fit(X_train, y_train.ravel())
        y_pred = models[i].predict(X_test).clip(min=0)
        plots.append(y_pred)
        print("%20s : %.3f" % (model_names[i], mean_squared_error(y_test, y_pred)))

    plt.plot(y_test, color='red', linewidth=4, label='ground truth')
    for i in range(0, len(plots)):
        plt.plot(plots[i], linewidth=2, label=model_names[i])
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
