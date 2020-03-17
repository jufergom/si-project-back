import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import json

#data_file = pd.read_csv("cost-of-living.csv")
#data_file = data_file.to_json()

#vars = ["Apartment (1 bedroom) in City Centre","Apartment (3 bedrooms) in City Centre"]

class ModelInformation:
    def __init__(self, precision, model):
        self.precision = precision
        self.model = model
    
    #converts class to json output
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

def error_model(y_test,y_model):
    #suma del error cuadrático
    error_c = ((y_model - y_test)**2).sum()
    #desviación
    desviacion = ((y_test - y_test.mean())**2).sum()

    #R_2

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
    #copy_data = data.rename(index=data.loc[:,data.columns[0]])
    #T_data = copy_data.drop(copy_data.columns[0],axis=1).T

    #X = T_data.iloc[:, 0]
    #Y = data.iloc[:, 3]

    X = data[ind_variables]
    Y = data[dep_variable]

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=tst_size)

    model_reg = linear_model.LinearRegression()

    model_reg.fit(X_train,y_train)

    y_model = model_reg.predict(X_test)

    error = error_model(y_test,y_model)

    # print("Precision % 5.5f \n" %(error))

    return ModelInformation(error, model_reg)


# obj = linear_regression(data_file, vars, 0.33)

# print("Precision: %f" %(obj.precision))