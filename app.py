from flask import Flask, escape, request, jsonify
from flask_cors import CORS
from users import users_api
import algorithms
import json

app = Flask(__name__)
CORS(app)

app.register_blueprint(users_api)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/linear', methods = ['GET'])
def linear_regression_endpoint():
    content = request.json
    variables = content['variables']
    parse_data = content['parseData']

    model = algorithms.linear_regression(json.dumps(parse_data), variables, 0.33)
    #print(type(model.precision))
    #print(model.precision.index[0])
    #print(type(model.precision.index[0]))
    #return str(model.precision.index[0].item())
    return jsonify(
        precision = model.precision.index[0].item()
    )

if __name__ == "__main__":
    app.run()