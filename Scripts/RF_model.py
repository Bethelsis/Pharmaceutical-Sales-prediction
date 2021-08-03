#!/usr/bin/env python
# coding: utf-8
# import necessary libraries
import numpy as np
import pandas as pd 
import datetime
from sklearn.impute import SimpleImputer
from sklearn import preprocessing 
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler, RobustScaler
from sklearn.linear_model import LinearRegression
from xgboost import XGBRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, accuracy_score,r2_score
import dvc.api
# ignore warnings
import warnings
warnings.filterwarnings(action="ignore")
#Load training data 
try:
    train_data=pd.read_csv("train.csv")
except FileNotFoundError:
        print("file not found")

#load test data
try:
    test_data=pd.read_csv("test.csv")
except FileNotFoundError:
     print("file not found")


#load store data
try:
    store_data=pd.read_csv("store.csv")
except FileNotFoundError:
        print("file not found")
# merge the train/test sets with the stores set
merged_train = pd.merge(left = train_data, right = store_data, how = 'inner', left_on = 'Store', right_on = 'Store')
merged_test = pd.merge(left = test_data, right = store_data, how = 'inner', left_on = 'Store', right_on = 'Store')


def preprocess_data(train, test):
    
    # '''preprocessing'''
    global train_features, test_features, train_target, categorical, numerical

    # train and target features
    train_features = train.drop(['Sales', 'Customers'], axis = 1) #drop the target feature + customers (~ will not be used for prediction)
    train_target  = train[['Sales']]
    test_features = test.drop(['Id'], axis = 1) #drop id, it's required only during submission

    #feature generation + transformations
    try:
        train_features['Date'] = pd.to_datetime(train_features.Date)
        train_features['Month'] = train_features.Date.dt.month.to_list()
        train_features['Year'] = train_features.Date.dt.year.to_list()
        train_features['Day'] = train_features.Date.dt.day.to_list()
        train_features['WeekOfYear'] = train_features.Date.dt.weekofyear.to_list()
        train_features['DayOfWeek'] = train_features.Date.dt.dayofweek.to_list()
        train_features['weekday'] = 1        # Initialize the column with default value of 1
        train_features.loc[train_features['DayOfWeek'] == 5, 'weekday'] = 0
        train_features.loc[train_features['DayOfWeek'] == 6, 'weekday'] = 0
        train_features = train_features.drop(['Store'], axis = 1)

        test_features['Date'] = pd.to_datetime(test_features.Date)
        test_features['Month'] = test_features.Date.dt.month.to_list()
        test_features['Year'] = test_features.Date.dt.year.to_list()
        test_features['Day'] = test_features.Date.dt.day.to_list()
        test_features['WeekOfYear'] = test_features.Date.dt.weekofyear.to_list()
        test_features['DayOfWeek'] = test_features.Date.dt.dayofweek.to_list()
        test_features['weekday'] = 1        # Initialize the column with default value of 1
        test_features.loc[test_features['DayOfWeek'] == 5, 'weekday'] = 0
        test_features.loc[test_features['DayOfWeek'] == 6, 'weekday'] = 0
        test_features = test_features.drop(['Store'], axis = 1)
    except KeyError:
        print("Column couldn't be found")

    # numerical and categorical columns (train set)
    categorical = []
    numerical = []
    timestamp = []

    for col in train_features.columns:
        if train_features[col].dtype == object:
            categorical.append(col)
        elif train_features[col].dtype in ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']:
            numerical.append(col)
        else:
            timestamp.append(col)

    # Keep selected columns only
    my_cols = categorical + numerical + timestamp
    train_features = train_features[my_cols].copy()
    test_features = test_features[my_cols].copy()
    features = pd.concat([train_features, test_features]) #merge the features columns for uniform preprocessing

    # change dtypes for uniformity in preprocessing
    features.CompetitionOpenSinceMonth = features.CompetitionOpenSinceMonth.astype('Int64') 
    features.CompetitionOpenSinceYear = features.CompetitionOpenSinceYear.astype('Int64')
    features.Promo2SinceWeek = features.Promo2SinceWeek.astype('Int64') 
    features.Promo2SinceYear = features.Promo2SinceYear.astype('Int64')
    features["StateHoliday"].loc[features["StateHoliday"] == 0] = "0"



    # ''' actual preprocessing: the mighty pipeline '''
    # numeric
    for col in ['CompetitionDistance', 'CompetitionOpenSinceMonth', 'CompetitionOpenSinceYear', 'Promo2SinceWeek', 'Promo2SinceYear']:
        features[col] = features[col].fillna((int(features[col].mean()))) 
    features.PromoInterval = features.PromoInterval.fillna(features.PromoInterval.mode()[0])
    features.Open = features.Open.fillna(features.Open.mode()[0])
    features = pd.get_dummies(features, columns=['StoreType', 'Assortment', 'PromoInterval', 'StateHoliday'])
    
    scaler = RobustScaler()
    c = ['DayOfWeek', 'Open', 'Promo', 'SchoolHoliday', 'CompetitionDistance', 'CompetitionOpenSinceMonth', 'CompetitionOpenSinceYear',
    'Promo2', 'Promo2SinceWeek', 'Promo2SinceYear', 'WeekOfYear', 'Month', 'Year', 'Day', 'WeekOfYear', 'weekday']
    features[numerical] = scaler.fit_transform(features[numerical].values)
   

    return features



features = preprocess_data(merged_train, merged_test)
features = features.drop(['Date'], axis = 1)


# reconstruct train and test sets
def reconstruct_sets(features):
    global x_train, x_val, y_train, y_val
    # global train_set
    # original train and test sets
    x_train = features.iloc[:len(train_features), :]
    x_test = features.iloc[len(train_features):, :]
    y_train = train_target
    # train_set = pd.concat([x_train, y_train], axis=1)

    # updated train and validation sets
    x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size = .20, random_state = 0)


    return x_train, x_val, y_train, y_val, x_test


x_train, x_val, y_train, y_val, x_test = reconstruct_sets(features)





clf=RandomForestRegressor(n_estimators=15)
clf.fit(x_train,y_train)
y_pred = clf.predict(x_val)
print("Mean squared error for RF on validation data =", mean_squared_error(y_val, y_pred))
print("Mean absolute error for RF on validation data =", mean_absolute_error(y_val, y_pred))
print("Mean R2 score for xgb on validation data =", r2_score(y_val, y_pred))







