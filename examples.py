from flask import Flask, escape, request, jsonify
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

#returns json of a simple person
@app.route('/person')
def persons():
    p1 = Person("John", 36)
    return p1.to_json()

#gets info from a post request

#returns a list of persons, doesnt work
@app.route('/persons')
def persons_list():
    persons = []
    p1 = Person("John", 36)
    p2 = Person("Hedmon", 3)
    persons.append(p1.to_json())
    persons.append(p2.to_json())
    return persons

if __name__ == "__main__":
    app.run()