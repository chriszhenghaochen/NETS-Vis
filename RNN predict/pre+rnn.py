"""
Test a whole bunch of predictors on data from Saturday
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from sklearn import tree, ensemble, naive_bayes, neighbors, dummy, cross_validation, svm
import script.predict.preprocess as pp
import matplotlib.pyplot as plt
import numpy as np
import data


import numpy as np
from sklearn import metrics
import pandas

import tensorflow as tf
from tensorflow.contrib import learn

FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_bool('test_with_fake_data', False,
                         'Test the example code with fake data.')

MAX_DOCUMENT_LENGTH = 41
EMBEDDING_SIZE = 50
n_words = 1692 + 189


def input_op_fn(x):
  """Customized function to transform batched x into embeddings."""
  # Convert indexes of words into embeddings.
  # This creates embeddings matrix of [n_words, EMBEDDING_SIZE] and then
  # maps word indexes of the sequence into [batch_size, sequence_length,
  # EMBEDDING_SIZE].
  word_vectors = learn.ops.categorical_variable(x, n_classes=n_words,
      embedding_size=EMBEDDING_SIZE, name='words')
  # Split into list of embedding per word, while removing doc length dim.
  # word_list results to be a list of tensors [batch_size, EMBEDDING_SIZE].
  word_list = learn.ops.split_squeeze(1, MAX_DOCUMENT_LENGTH, word_vectors)
  return word_list




# Build model: a single direction GRU with a single layer
RNNclassifier = learn.TensorFlowRNNClassifier(
    rnn_size=EMBEDDING_SIZE, n_classes=5, cell_type='gru',
    input_op_fn=input_op_fn, num_layers=1, bidirectional=False,
    sequence_length=None, steps=1000, optimizer='Adam',
    learning_rate=0.01, continue_training=True)

DNNclassifier = learn.DNNClassifier(hidden_units=[10, 10], n_classes=5)

##################################predict#############################################
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
    'Random':
        dummy.DummyClassifier(strategy='stratified'),
    'Most Frequent':
        dummy.DummyClassifier(strategy='most_frequent'),
    'Uniform':
        dummy.DummyClassifier(strategy='uniform'),
    'RNN':
        RNNclassifier,
    # 'DNN':
    #     DNNclassifier
}

categories = ['Thrill Rides',
              'Kiddie Rides',
              'Rides for Everyone',
              'Shows and Entertainment',
              'Shopping']
x, y = pp.get_bag_data(['Sat'], 16, categories=categories)
x = (x > 0).astype('int64')
kp = data.read_key_points().set_index('place_id')
kp = kp[kp['category'].isin(categories)]
kp['category'] = kp['category'].astype('category')
y = kp.loc[y, 'category'].cat.codes.values

x_train, x_validate, y_train, y_validate = cross_validation.train_test_split(x, y, train_size=0.90,
                                                                             random_state=294967295)


# y_train_cats = kp.loc[y_train, 'category'].cat.codes.values

scorings = ['accuracy', 'log_loss']
names = []
scores = {}




def plot_scores():
    fig, axs = plt.subplots(len(scorings), 1)
    for scoring, ax, color in zip(scorings, axs, data.palette10):
        score_mean_list = [scores[n][scoring]['mean'] for n in names]
        score_std_list = [scores[n][scoring]['std'] for n in names]

        if ax is None:
            fig, ax = plt.subplots()
        width = 0.75
        ind = np.arange(len(names))
        ax.bar(ind + (0.5 * width), score_mean_list, width, yerr=score_std_list, color=color, error_kw=dict(ecolor='black'))
        ax.set_xticks(ind + width)
        ax.set_xticklabels(names)
        ax.set_title('Scoring = {}'.format(scoring))


def test_classifier(clf, name):
    if name not in names:
        names.append(name)
    score_dict = {}
    for scoring in scorings:
        print('scoring = {}'.format(scoring))

        if(name == 'RNN'):
            RNNclassifier.fit(x_train, y_train, steps=100)
            y_predicted = RNNclassifier.predict(x_validate)
            score = metrics.accuracy_score(y_validate, y_predicted)

            score_dict[scoring] = {
                'mean': score,
                'std': 0
            }

            print(score)

        # elif(name == 'DNN'):
        #     x_sub_train = np.array(x_train, dtype = 'int32')
        #     y_sub_train = np.array(y_train, dtype = 'int32')
        #     x_sub_test = np.array(x_validate, dtype = 'int32')
        #     y_sub_test =np.array(y_validate, dtype = 'int32')
        #
        #     DNNclassifier.fit(x_sub_train, y_sub_train, steps=100)
        #     score = metrics.accuracy_score(y_sub_test, DNNclassifier.predict(x_sub_test))
        #     score_dict[scoring] = {
        #         'mean': score,
        #         'std': 0
        #     }

        else:
            score = cross_validation.cross_val_score(clf, x_train, y_train, cv=5, scoring=scoring)
            score_dict[scoring] = {
                'mean': score.mean(),
                'std': score.std()
            }
            print(score.mean())

    scores[name] = score_dict


def main():
    # for name in ['Most Frequent', 'Uniform', 'KNN', 'Decision Tree', 'MultinomialNB', 'SVM', 'Random Forest', 'RNN', 'DNN']:
    for name in ['Most Frequent', 'Uniform', 'KNN', 'Decision Tree', 'MultinomialNB', 'SVM', 'Random Forest', 'RNN']:
        print(name)
        test_classifier(predictors[name], name)
    # for name, clf in sorted(predictors.items()):
    #     print(name)
    #     test_classifier(clf, name)
    # test_classifier(svm.SVC(kernel='rbf', gamma=0.7, C=1, probability=True), 'svc')

    plot_scores()

    plt.savefig('predictions.png', tight=True)
    plt.show()


if __name__ == '__main__':
    main()

