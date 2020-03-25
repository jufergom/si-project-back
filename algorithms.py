import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report,confusion_matrix
import json

class ModelInformation:
    def __init__(self, precision, responseText, model):
        self.precision = precision
        self.responseText = responseText
        self.model = model
    
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

def error_model(y_test,y_model):
    error_c = ((y_model - y_test)**2).sum()
    desviacion = ((y_test - y_test.mean())**2).sum()
    R_2 = 1 - (error_c/desviacion)
    return R_2

''' 
    - file is a json that contains the Data to be evaluated (JSON)
    - independent variables is an array that contains strings 
      to the names of the columns to be evaluated (String[])
    - tst_size is the portion of the data that is to be used to train
      the model (int)
'''
def linear_regression(file, ind_variables, dep_variable, tst_size):
    data = pd.read_json(file, orient='records')
    X = data[ind_variables]
    Y = data[dep_variable]

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=tst_size)
    X_test = X_test.fillna(X_test.mean())
    X_train = X_train.fillna(X_train.mean())
    y_train = y_train.fillna(y_train.mean())
    #y_test = y_test.fillna(y_test.mean())

    model_reg = linear_model.LinearRegression()
    model_reg.fit(X_train, y_train)
    y_model = model_reg.predict(X_test)
    
    error = error_model(y_test,y_model)

    response = "Modelo Producido [" + "f(x) = " + str(model_reg.coef_[0]) + "x + " + str(model_reg.intercept_) + "] Precision [" + str(error) + "]"
    return ModelInformation(error, response, model_reg)
    
def logistic_regression(file, type_variable, tst_size):
    data = pd.read_json(file, orient='records')
    tX = data.drop([type_variable[0].decode('utf_8')],1)
    tY = data[type_variable[0].decode('utf_8')]
    
    X = np.array(tX)
    X = X[:-1]
    Y = np.array(tY)
    Y = Y[:-1]
    
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=tst_size)
    
    model_reg = linear_model.LogisticRegression()
    model_reg.fit(X_train, Y_train)
    y_model = model_reg.predict(X_test)
    
    error = 1 - (y_model!=Y_test).sum()/len(y_model)
    
    response = "Coeficientes Modelo Producido " + str(model_reg.coef_) + " Precision [" + str(error) + "]"
    return ModelInformation(error, response, model_reg)

def clustering(file, numberOfClusters, type_variable):
    data = pd.read_json(file, orient='records')
    X = data.drop([type_variable[0].decode('utf_8')],1)
    Y = data[type_variable[0].decode('utf_8')]
    
    X = X[:-1]
    Y = Y[:-1]
    
    KM_clusters = KMeans(n_clusters=numberOfClusters, init='k-means++').fit(X)
    KM_clustered = X.copy()
    KM_clustered.loc[:,'Cluster'] = KM_clusters.labels_
    
    KM_clust_sizes = KM_clustered.groupby('Cluster').size().to_frame()
    KM_clust_sizes.columns = ["KM_size"]
    sizes = KM_clust_sizes["KM_size"]
        
    error = 1 - abs(Y - KM_clustered.Cluster).sum()/len(Y)
    
    response = "Se crearon " + str(numberOfClusters) + " clusters, con volumenes ["
    
    for size in sizes:
        response = response + str(size) + ","
        
    response = response[:-1]
    response = response + "] Precision [" + str(error) + "]"
    
    model = {}
    return ModelInformation(error, response, model)

def clustering_noprec(file, numberOfClusters):
    data = pd.read_json(file, orient='records')
    
    X = X[:-1]
    Y = Y[:-1]
    
    KM_clusters = KMeans(n_clusters=numberOfClusters, init='k-means++').fit(X)
    KM_clustered = X.copy()
    KM_clustered.loc[:,'Cluster'] = KM_clusters.labels_
    
    KM_clust_sizes = KM_clustered.groupby('Cluster').size().to_frame()
    KM_clust_sizes.columns = ["KM_size"]
    sizes = KM_clust_sizes["KM_size"]
    response = "Se crearon " + str(numberOfClusters) + " clusters, con volumenes ["
    
    for size in sizes:
        response = response + str(size) + ","

    error = 0
    model = {}
    return ModelInformation(error, response, model)


def neural_network(file,outputVariable,hidden_layers_1,hidden_layers_2,activationFunction,numberOfIterations,tst_size):
    data = pd.read_json(file, orient='records')
    X = data.drop([outputVariable.decode('utf_8')],1)
    Y = data[outputVariable.decode('utf_8')]
    
    X = X[:-1]
    Y = Y[:-1]
    
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=tst_size)
    
    mlp = MLPClassifier(hidden_layer_sizes=(hidden_layers_1,hidden_layers_2), activation = activationFunction, max_iter = numberOfIterations)
    mlp.fit(X_train,Y_train)
    
    predictions = mlp.predict(X_test)
    
    confusionMatrix = confusion_matrix(Y_test, predictions)
    
    error = 1
    model = {}
    response = "Confusion Matrix " + str(confusionMatrix)
    return ModelInformation(error, response, model)