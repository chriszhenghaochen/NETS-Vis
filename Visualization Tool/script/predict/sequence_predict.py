import data
import numpy as np
from datetime import datetime
import script.predict.predict as predict
import time


def get_data(days=None, cutoff_hour=12, categories=None, length=3):
    x_ts = []
    y_ts = []
    xs = []
    ys = []
    print('Getting data')
    for day in days:
        print(day)
        df = data.read_visited_key_points(day, extra=['category'], grouped=True)
        if categories is not None:
            df = df[df['category'].isin(categories)]

        first_time = df['Timestamp'].min()
        cutoff = datetime(first_time.year, first_time.month, first_time.day, cutoff_hour)
        # df_pre = df[df['Timestamp'] <= cutoff].sort_values('Timestamp').copy()
        # df_pre['reverse_order_visited'] = df_pre.groupby('group_id', sort=False).cumcount(ascending=False)
        for name, group in df.groupby('group_id'):
            group = group.sort_values('Timestamp')
            places = group.loc[group['Timestamp'] <= cutoff, 'place_id'].values
            if len(places) <= length:
                continue
            x = places[-length:]
            after = group.loc[group['Timestamp'] > cutoff, 'place_id'].values
            if len(after) == 0:
                y = 0
            else:
                y = after[0]

            x_t = np.array([places[i:i+length] for i in range(len(places)-length)])
            y_t = np.array([places[i+length] for i in range(len(places)-length)])

            x_ts.append(x_t)
            y_ts.append(y_t)
            xs.append(x)
            ys.append(y)

    x_ts = np.concatenate(x_ts, axis=0)
    y_ts = np.concatenate(y_ts, axis=0)
    xs = np.array(xs)
    ys = np.array(ys)

    return x_ts, y_ts, xs, ys


def main():
    # Code duplication here but I can't think how to avoid it
    categories = ['Thrill Rides', 'Kiddie Rides', 'Rides for Everyone', 'Shows & Entertainment', 'Shopping']

    x_t, y_t, x, y = get_data(['Fri'], 12, categories=categories, length=5)
    method_names = ['Decision Tree', 'MultinomialNB', 'GaussianNB', 'KNN', 'Shuffle']
    predictors = [predict.decision_tree_predict,
                  predict.mnb_predict,
                  predict.gnb_predict,
                  predict.knn_predict,
                  predict.shuffle_predictor]
    averaging_times = 4
    # I think this could cause an error if there was a category in the test data that wasn't in the training data
    cats = len(np.unique(y))

    for name, function in zip(method_names, predictors):
        print(name)
        t0 = time.clock()
        p = function(x_t, y_t)
        y_out = p.predict(x)
        t1 = time.clock()
        print('  Accuracy = {}'.format(np.mean(y == y_out)))
        print('  Time = {}'.format(t1-t0))

if __name__ == '__main__':
    main()