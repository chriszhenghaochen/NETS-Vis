from sklearn import tree, naive_bayes, neighbors, dummy, ensemble

# ----------------- Prediction Functions ------------------

all_predictors = {
    # 'Decision Tree':
    #     tree.DecisionTreeClassifier(),
    # 'Gradient Boosting':
    #     ensemble.GradientBoostingClassifier(n_estimators=33, learning_rate=1.0, random_state=0),
    'Random Forest':
        ensemble.RandomForestClassifier(max_depth=2),
    'Adaboost':
        ensemble.AdaBoostClassifier(random_state=0),
    'MultinomialNB':
        naive_bayes.MultinomialNB(),
    # 'GaussianNB': gnb_predict,
    'BernoulliNB':
        naive_bayes.BernoulliNB(),
    # 'KNN':
    #     neighbors.KNeighborsClassifier(n_neighbors=10),
    # 'Random':
    #     dummy.DummyClassifier(strategy='stratified'),
    'Most Frequent':
        dummy.DummyClassifier(strategy='most_frequent'),
    'Uniform':
        dummy.DummyClassifier(strategy='uniform')
}