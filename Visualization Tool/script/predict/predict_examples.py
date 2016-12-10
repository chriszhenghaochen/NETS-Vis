import data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import script.predict.preprocess as pp
from sklearn import ensemble, cross_validation

# ----------- Part 1: Getting data to predict -----------
# the categories we want to use to predict (so, we don't both trying to predict if people go the the bathroom)
categories = ['Thrill Rides', 'Kiddie Rides', 'Rides for Everyone', 'Shows & Entertainment', 'Shopping']

# this calls a function in script.predict.preprocess that gets some data
# x = data from previous places they've been
# y = next place
# prev = the last place they were at
# ids = the group id of each row in x & y
x, y, prev, ids = pp.get_bag_data(['Fri'], 11, categories, return_prev=True, return_ids=True)

# I made the ids only include data about which day it is, as group 0 is a different group on Friday and Saturday
# Because we're only looking at Friday, I'm discarding that data.
ids = ids['group_id'].values
# clamp x values to 1 or 0. This means that if a person visited a ride there will be a 1, otherwise there will
# be a zero
x = (x > 0).astype('int64')

# ----------- Part 2: Splitting the data -----------
# training data -> data used to build the model
# testing data -> data used to see if the model is good
x_train, x_test, y_train, y_test, prev_train, prev_test, ids_train, ids_test = (
    cross_validation.train_test_split(x, y, prev, ids, train_size=0.25, random_state=0)
)

# ----------- Part 3: Predicting -----------
# here we use the random forest classifier. If you want to use another classifier from
# scikit, you can replace this with another one. If you wanted to do something with neural
# networks you'll need to use another library, but the same data
predictor = ensemble.RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)
# here's an example using naive bayes
# predictor = naive_bayes.MultinomialNB()

# train the model
predictor.fit(x_train, y_train)

# using the model, try predicting the next place people are going to go
y_pred = predictor.predict(x_test)

# now we're looking at the probability of someone going to each ride
# the rows correspond to each trajectory, and the columns are the rides.
# To figure out which column is which ride, you look at predictor.classes_
y_probs = predictor.predict_proba(x_test)


# if you want to look at the prediction of a single person, you can do something like

# this returns a vector with true or false depending on whether each element is 340
# you can then use this to pick out the right part of the other vectors
ids_test == 340

# pick out the data we used to predict where the person will go next
data = x_test[ids_test == 340]
# pick out the model's prediction of where they will go
prediction = y_pred[ids_test == 340]
# pick out the model's prediction of the probabilities of them going to different places
probabilty_prediction = y_probs[ids_test == 340]
# pick out where they actually went
actual = y_test[ids_test == 340]

print(data)
print(prediction)
print(probabilty_prediction)
print(actual)