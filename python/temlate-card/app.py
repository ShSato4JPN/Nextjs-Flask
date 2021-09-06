from flask import Flask
from flask import make_response, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    res = {
        "username":"satoshi",
        "age":"26",
        "email":"satoshi.2021@example.com"
    }

    return jsonify(res)

if __name__ == '__main__':
    app.run(host='192.168.1.30')