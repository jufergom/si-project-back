from flask import Flask, escape, request, jsonify, Response
import json
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    #converts class to json output
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

def get_connection():
    cnx = mysql.connector.connect(
        host="bfzkzkyq0abmhdbsc2ru-mysql.services.clever-cloud.com",
        user="ubhjonh4iskqwirm",
        passwd="CYc3hNVQBPe2tbFx1ZKB",
        database="bfzkzkyq0abmhdbsc2ru"
    )
    return cnx

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/mysql')
def connection_test():
    cnx = get_connection()
    cursor = cnx.cursor()

    query = ("SELECT * FROM users")
    cursor.execute(query)
    row_headers=[x[0] for x in cursor.description] #this will extract row headers
    rv = cursor.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    return json.dumps(json_data)

#returns status ok (200) if credentials are correct, otherwise returns status no content (204)
#expected contents of received json: username, password
@app.route('/api/login', methods = ['POST'])
def login():
    content = request.json
    r_email = content['email']
    r_password = content['password']
    cnx = get_connection()
    cursor = cnx.cursor()

    query = ("SELECT email, password FROM users WHERE email = %s AND password = %s")
    cursor.execute(query, (r_email, r_password))
    resp = Response(status=204, mimetype='application/json')
    for (email, password) in cursor:
        if email == r_email and password == r_password:
            resp = Response(status=200, mimetype='application/json')
        else:
            resp = Response(status=204, mimetype='application/json')
    #if content['username'] == "jufergom" and content['password'] == "1234":
        #resp = Response(status=200, mimetype='application/json')
    #else:
        #resp = Response(status=204, mimetype='application/json')
    return resp

if __name__ == "__main__":
    app.run()