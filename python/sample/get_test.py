from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    return """
        <html><body>
        <form action="/hello" method="GET">
          name:<input type="text" name="name" />
          <input type="submit" value="submit" />
        </form>
        </body></html>
    """

@app.route('/test')
def test():
    return 'hello'


@app.route('/hello')
def hello():
    name = request.args.get('name')
    if name is None: name='nanashi'
    return """
        <h1>mr. {0}, hello</h1>
    """.format(name)

if __name__ == '__main__':
    app.run(debug=True, host='192.168.1.30')
