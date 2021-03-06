from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    a = request.args.get('a')
    b = request.args.get('b')

    if ( a is None ) or ( b is None ):
        return 'parameter is not enough'
    
    c = int(a) * int(b)

    return '<h1>' + str(c) + '</h1>'

if __name__ == '__main__':
    app.run(debug=True, host='192.168.1.30')