from sklearn import tree, ensemble, naive_bayes, neighbors, dummy, cross_validation, svm
import matplotlib.pyplot as plt
import numpy as np
import data
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn import svm
from sklearn.cross_validation import train_test_split
from rnnclass import RNN
import matplotlib.pyplot as plt;

plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt




length = 359
objects  = ('Most Frequent', 'Uniform', 'KNN', 'Decision Tree', 'MultinomialNB', 'SVM', 'Random Forest', 'RNN')
y = []



if 1:
    predictors = {
        'Decision Tree':
            tree.DecisionTreeClassifier(),
        'Gradient Boosting':
            ensemble.GradientBoostingClassifier(n_estimators=100, max_depth=2, learning_rate=1.0, random_state=0),
        'Random Forest':
            ensemble.RandomForestClassifier(max_depth=2, random_state=0),
        'Adaboost':
            ensemble.AdaBoostClassifier(random_state=0),
        'MultinomialNB':
            naive_bayes.MultinomialNB(),
        # 'GaussianNB': gnb_predict,
        'BernoulliNB':
            naive_bayes.BernoulliNB(),
        'KNN':
            neighbors.KNeighborsClassifier(n_neighbors=10),
        'SVM':
            svm.SVC(kernel='rbf', gamma=0.7, C=1, probability=True),
        # 'Random':
        #     dummy.DummyClassifier(strategy='stratified'),
        'Most Frequent':
            dummy.DummyClassifier(strategy='most_frequent'),
        'Uniform':
            dummy.DummyClassifier(strategy='uniform')
    }


    #----------------------------------------------preprocessing--------------------------------------------------------#

    file = pd.read_csv('rnn3.csv')
    dim = np.arange(length).astype(str)


    #train
    label = file[str(length)].values.astype(int)
    data= np.asarray(file[dim].values/101)

    X_train, X_test, y_train, y_test = train_test_split(
        data, label, test_size=0.2, random_state=294967295)


    for name in ['Most Frequent', 'Uniform', 'KNN', 'Decision Tree', 'MultinomialNB', 'SVM', 'Random Forest']:
        clf = predictors[name].fit(X_train, y_train)
        score = clf.score(X_test, y_test)

        y.append(score)
        print(score)


    rnn = RNN(length = length)
    score = rnn.scores
    y.append(score[1])

    print(y)
    y_pos = np.arange(len(objects))
    y1 = np.asarray(y)

    plt.bar(y_pos, y1*100, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Accuracy')
    plt.title('Prediction Method')

    plt.show()

# plt.show()