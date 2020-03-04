from flask import Flask, escape, request
from flask_cors import CORS
from users import users_api

app = Flask(__name__)
CORS(app)

app.register_blueprint(users_api)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

if __name__ == "__main__":
    app.run()