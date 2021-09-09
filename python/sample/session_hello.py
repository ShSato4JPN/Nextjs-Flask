from flask import Flask, request, session, redirect
app = Flask(__name__)
app.secret_key = 'zono3104'

@app.route('/')
def index():
    return """
    <html><body><h1>input user name</h1>
    <form action="/setname" method="GET">
    name:<input type="text" name="username" />
    <input type="submit" value="start" />
    </form>
    </body></html>
    """

@app.route('/setname')
def setname():
    name = request.args.get('username')
    if name is None: return redirect('/')
    session['name'] = name
    return redirect('/morning')

def getLinks():
    return """
    <ul><li><a href="/morning">in morning</a></li>
    <li><a href="/hello">in noon</a></li>
    <li><a href="/night">in night</a></li></ul>
    """

@app.route('/morning')
def morning():
    if not ('name' in session):
        return redirect('/')
    
    name = session['name']
    return """
    <h1>good morning mr.{0}</h1>{1}
    """.format(name, getLinks())

@app.route('/hello')
def hello():
    if not ('name' in session):
        return redirect('/')
    
    name = session['name']
    return """
    <h1>hello mr.{0}</h1>{1}
    """.format(name, getLinks())

@app.route('/night')
def night():
    if not ('name' in session):
        return redirect('/')
    
    name = session['name']
    return """
    <h1>good evening mr.{0}</h1>{1}
    """.format(name, getLinks())

if __name__ == '__main__':
    app.run(host='192.168.1.30')