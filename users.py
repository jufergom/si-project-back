from flask import Blueprint, escape, request, jsonify, Response
import json
import mysql.connector
from mysql.connector import Error

users_api = Blueprint('users_api', __name__)

def get_connection():
    cnx = mysql.connector.connect(
        host="bfzkzkyq0abmhdbsc2ru-mysql.services.clever-cloud.com",
        user="ubhjonh4iskqwirm",
        passwd="CYc3hNVQBPe2tbFx1ZKB",
        database="bfzkzkyq0abmhdbsc2ru"
    )
    return cnx

#returns status ok (200) if credentials are correct, otherwise returns status not found (404)
#expected contents of received json: username, password
@users_api.route('/api/login', methods = ['POST'])
def login():
    content = request.json
    username = content['username']
    password = content['password']
    cnx = get_connection()
    cursor = cnx.cursor()

    args = [username, password, 0]
    result = cursor.callproc("check_password", args)
    resp = Response(status=404, mimetype='application/json') #if credentials are incorrect
    #if count == 1, then user credentials are correct
    if result[2] == 1:
        resp = Response(status=200, mimetype='application/json')
    cnx.close()
    cursor.close()
    return resp

@users_api.route('/api/user/createUser', methods = ['POST'])
def create_user():
    try:
        content = request.json
        username = content['username']
        password = content['password']
        cnx = get_connection()
        cursor = cnx.cursor()

        args = [username, password]
        cursor.callproc("create_user", args)
        cnx.commit()
        resp = Response(status=200, mimetype='application/json') #status: success
    except Error as e:
        print(e)
        resp = Response(status=400, mimetype='application/json') #bad request
    finally:
        cnx.close()
        cursor.close()
        return resp