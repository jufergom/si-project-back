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
    print(ind_variables)
    dep_variable = content['selectedVariableDependent']
    print(dep_variable)
    parse_data = content['parseData']

    model = algorithms.linear_regression(json.dumps(parse_data), ind_variables, dep_variable,0.2)
    print(model.precision)
    print(type(model.precision))
    return jsonify(
        precision = model.precision.item()
    )

if __name__ == "__main__":
    application.run()