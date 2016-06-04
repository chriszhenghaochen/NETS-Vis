import matplotlib
matplotlib.use('Qt4Agg')
import data
import pandas as pd
import matplotlib.pyplot as plt
import script.predict.preprocess as pp
import script.predict.predictors as pdt
from sklearn.cross_validation import train_test_split

training_size = 0.25
x, y = pp.get_bag_data(['Sat'], 12, pp.common_categories)
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=training_size, random_state=2294967295)

im = data.read_image(size=1000)
for predictor_name in pdt.all_predictors:
    predictor = pdt.all_predictors[predictor_name]
    predictor.fit(x_train, y_train)
    y_pred = predictor.predict(x_test)
    y_pred_probs = predictor.predict_proba(x_test)

    kp = data.read_key_points().set_index('place_id')
    # Adjust the size of this so that it's proportional to the testing data
    kp['Training Counts'] = ((1 - training_size) / training_size) * pd.Series(y_train).value_counts()
    kp['Test Counts'] = pd.Series(y_test).value_counts()
    kp['Prediction Counts'] = pd.Series(y_pred).value_counts()
    kp['Prediction Probability Sum'] = pd.DataFrame(y_pred_probs, columns=predictor.classes_).sum()
    kp.fillna(0, inplace=True)

    # fig, axs = plt.subplots(2, 2)
    fig, axs = plt.subplots(1, 3)
    fig.suptitle(predictor_name)

    # titles = ['Training Counts', 'Test Counts', 'Prediction Counts', 'Prediction Probability Sum']
    titles = ['Test Counts', 'Prediction Counts', 'Prediction Probability Sum']
    for ax, title in zip(axs.flat, titles):
        ax.imshow(im, extent=[0, 100, 0, 100])
        ax.scatter(x=kp['X'], y=kp['Y'], s=kp[title])
        ax.set_title(title)

    figManager = plt.get_current_fig_manager()
    # Qt4Agg specific
    figManager.window.showMaximized()
    fig.tight_layout()

plt.show()