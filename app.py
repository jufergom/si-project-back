from flask import Flask, escape, request, jsonify, Response
import json

app = Flask(__name__)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    #converts class to json output
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

#returns status ok (200) if credentials are correct, otherwise returns status no content (204)
#expected contents of received json: username, password
@app.route('/api/login', methods = ['POST'])
def login():
    content = request.json
    if content['username'] == "jufergom" and content['password'] == "1234":
        resp = Response(status=200, mimetype='application/json')
    else:
        resp = Response(status=204, mimetype='application/json')
    return resp

if __name__ == "__main__":
    app.run()