from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    jsonData = {
        "username":"satoshi",
        "age":"26",
        "email":"satoshi.hokazono@sample.com"
    }
    return jsonData

if __name__ == '__main__':
    app.run(debug=True, host='192.168.1.30')
