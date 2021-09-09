from flask import Flask, request, redirect
import os
app = Flask(__name__)

DATAFILE = './borad-data.txt'

@app.route('/')
def index():
    msg = 'no data'
    if os.path.exists(DATAFILE):
        with open(DATAFILE, 'rt') as f:
            msg = f.read()
    return """
    <html><body>
    <h1>message board</h1>
    <div style="background-color:yellow;padding:3em">
    {0}</div>
    <h3>update of borad message</h3>
    <form action="/write" method="POST">
    <textarea name="msg" rows="6" cols="60"></textarea><br/>
    <input type="submit" value="write">
    </form>
    </body></html>
    """.format(msg)

@app.route('/write', methods=['POST'])
def write():
    if 'msg' in request.form:
        msg = str(request.form['msg'])
        with open(DATAFILE, 'wt') as f:
            f.write(msg)
    return redirect('/')

@app.route('/users/<user_id>')
def users(user_id):
    return "user {0} 's page!!".format(user_id)

if __name__ == '__main__':
    app.run(host='192.168.1.30')