from flask import Flask, escape, request, jsonify
from flask_cors import CORS
from users import users_api
import algorithms
import json

application = Flask(__name__)
CORS(application)

application.register_blueprint(users_api)

@application.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@application.route('/linear', methods = ['POST'])
def linear_regression_endpoint():
    content = request.json
    ind_variables = content['selectedVariablesIndependent']
    dep_variable = content['selectedVariableDependent']
    parse_data = content['parseData']

    model = algorithms.linear_regression(json.dumps(parse_data), ind_variables, dep_variable,0.2)
    return jsonify(
        precision = model.precision.item(),
        responseText = model.responseText
    )
    
@application.route('/logistic', methods = ['POST'])
def logistic_regression_endpoint():
    content = request.json
    typ_variable = content['selectedVariableType']
    parse_data = content['parseData']

    model = algorithms.logistic_regression(json.dumps(parse_data), typ_variable, 0.2)
    return jsonify(
        precision = model.precision,
        responseText = model.responseText
    )
    
@application.route('/clustering', methods = ['POST'])
def clustering_endpoint():
    content = request.json
    number_clusters = content['numberCluster']
    typ_variable = content['selectedVariableType']
    parse_data = content['parseData']
    
    model = algorithms.clustering(json.dumps(parse_data), number_clusters, typ_variable)
    return jsonify(
        precision = model.precision,
        responseText = model.responseText
    )
    
@application.route('/neuralnetwork', methods = ['POST'])
def neural_network_endpoint():
    content = request.json
    output_variable = content['outputVariable']
    hidden_layers_size_1 = content['hiddenLayers1']
    hidden_layers_size_2 = content['hiddenLayers2']
    activation_function = content['activationFunction']
    number_iterations = content['numberOfIterations']
    parse_data = content['parseData']
    
    model = algorithms.neural_network(json.dumps(parse_data),output_variable,hidden_layers_size_1,hidden_layers_size_2,activation_function,number_iterations,0.2)
    return jsonify(
        precision = model.precision,
        responseText = model.responseText
    )
    
if __name__ == "__main__":
    application.run()