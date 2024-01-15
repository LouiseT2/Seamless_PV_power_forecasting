import tarfile
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import neighbors, datasets, preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import seaborn as sns
from dtw import *
from fastdtw import fastdtw
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
import gmdh
from gmdh import Combi
from statsmodels.tsa.api import AutoReg
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from sklearn.model_selection import GridSearchCV
from graph import *
from sklearn.model_selection import TimeSeriesSplit

def columns_selection(Sat_num,Kc=True):
    columns=['Sirta_GHI', 'Clearsky_GHI','Arpege_GHI', 'SZA','Wreg_1.0', 'Wreg_2.0', 'Wreg_3.0', 'Wreg_4.0','Sirta_GHI_T0-1j']
    if Kc:
        columns.extend(['Kc_Sat_mean','Kc_Sat_std', 'Kc_obs'])
    sat_name="Sat_GHI_T0+{}"
    for n in Sat_num:
        columns.append(sat_name.format(n))
    return columns


#Predictions:
def model_fit_prediction(train_data,test_data, model):
    X_train=train_data.drop('Sirta_GHI',axis='columns')
    Y_train=train_data['Sirta_GHI']
    X_test=test_data.drop('Sirta_GHI',axis='columns')
    Y_test=test_data['Sirta_GHI']
    scaler = preprocessing.StandardScaler().fit(X_train)
    X_train_scaler = scaler.transform(X_train)
    X_test_scaler = scaler.transform(X_test)
    model.fit(X_train_scaler, Y_train)
    Y_pred= model.predict(X_test_scaler)
    return X_train,Y_train,X_test,Y_test,Y_pred,model


def try_sat(model,train_data,test_data,div=1):
    index_sat=list(range(360,-1,-15*div))
    results = {'Index': [], 'MSE': [], 'MAE': [], 'R2': [], 'DTW': []}
    for i in index_sat:
        train=train_data[columns_selection([i],False)]
        test=test_data[columns_selection([i],False)]
        data=model_fit_prediction(train,test, model)
        evaluation=evaluate_algo(model,data[3],data[4])
        results['Index'].append(i)
        results['MSE'].append(evaluation[0])
        results['MAE'].append(evaluation[1])
        results['R2'].append(evaluation[2])
        results['DTW'].append(evaluation[3])
        print(i)

    results_df = pd.DataFrame(results)
    return results_df

#Test:
def test_hyperparameters(algo,parameters,standardized_X,Y_train):
    grid=GridSearchCV(estimator=algo,param_grid=parameters,n_jobs=-1)
    grid.fit(standardized_X,Y_train)
    return grid.best_score_,grid.best_estimator_


#Mesures:
def evaluate_algo(model,Y_test,Y_pred):
    MSE=mean_squared_error(Y_test, Y_pred)
    MAE=mean_absolute_error(Y_test, Y_pred)
    R2=r2_score(Y_test, Y_pred)
    distance, path = fastdtw(Y_test, Y_pred)
    print(model)
    print("MSE:", MSE)
    print("MAE:", MAE)
    print("R-squared:", R2)
    print("Distance DTW:",distance)
    return MSE,MAE,R2,distance
    
def cross_val(model,X,y,graph=True):
    tscv=TimeSeriesSplit()
    for train_index, test_index in tscv.split(X):
        X_train, X_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = y.iloc[train_index], y.iloc[test_index]

        # Fit the model on the training data
        model.fit(X_train, y_train)

        # Make predictions on the test data
        y_pred = model.predict(X_test)
    
        if graph:
            train_test_split_graph(y_train,y_test)
            features_importance(model, X_train)
        
        evaluate_algo(model,y_test,pd.Series(y_pred))