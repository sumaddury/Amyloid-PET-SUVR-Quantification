"""
Code for Gradient Boosting Decision Tree
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import lightgbm
import seaborn as sns
from sklearn.metrics import mean_squared_error


train_df = pd.read_csv("...\\Full Set\\GBDTTrain.csv")
test_df = pd.read_csv("...\\Full Set\\GBDTTest.csv")


# Fill in missing values
train_df["APOE A1"].fillna(value = train_df["APOE A1"].median(), inplace = True)
train_df["APOE A2"].fillna(value = train_df["APOE A2"].median(), inplace = True)
train_df["MMSE Total Score"].fillna(value = train_df["MMSE Total Score"].median(), inplace = True)
train_df["FAQ Total Score"].fillna(value = train_df["FAQ Total Score"].median(), inplace = True)

test_df["APOE A1"].fillna(value = test_df["APOE A1"].median(), inplace = True)
test_df["APOE A2"].fillna(value = test_df["APOE A2"].median(), inplace = True)
test_df["MMSE Total Score"].fillna(value = test_df["MMSE Total Score"].median(), inplace = True)
test_df["FAQ Total Score"].fillna(value = test_df["FAQ Total Score"].median(), inplace = True)


# Construct datasets
X_train = train_df.drop(columns=['ID', 'Value'])
y_train = train_df['Value']

X_test = test_df.drop(columns=['ID', 'Value'])
y_test = test_df['Value']


# Convert datasets to proprietary lightgbm format
features = [col for col in X_train]

# Categorical features must be specified
train_data = lightgbm.Dataset(X_train, label = y_train, feature_name = features, categorical_feature=['Gender', 'APOE A1', 'APOE A2'])
test_data = lightgbm.Dataset(X_test, label = y_test, feature_name = features, categorical_feature=['Gender', 'APOE A1', 'APOE A2'])


# Parameters were found through grid search
parameters = {'objective' : 'regression',
              'metric' : 'l1',
              'boosting_type' : 'gbdt',
              'max_depth' : 9,
              'feature_fraction' : 0.5,
              'learning_rate' : 0.045,
              'verbose' : 1
}

# Train with early stopping for max 50,000 iterations
GBM = lightgbm.train(parameters,
                      train_data,
                      valid_sets = test_data,
                      num_boost_round = 50000,
                      early_stopping_rounds = 500
                      )



# Make master pred and actual lists

GBDT_test_preds = list(GBM.predict(X_test))
GBDT_train_preds = list(GBM.predict(X_train))

GBDT_preds = GBDT_test_preds + GBDT_train_preds

GBDT_actual = list(y_test) + list(y_train)

GBDT_pred_actual = [[(GBDT_preds[i]), GBDT_actual[i]] for i in range(0,len(GBDT_preds))]

# Plot using seaborn

predactual = pd.DataFrame(GBDT_pred_actual, columns = ['Predicted', 'Actual'])
predactual.head()

sns.set(font_scale=1)
sns.set_style("whitegrid", {'axes.grid' : False})
plot = sns.regplot(x="Actual", y="Predicted", data=predactual, line_kws={"color": "red", 'alpha' : 0.33}, scatter_kws={'alpha':0.2});
plot.set_box_aspect(1)
