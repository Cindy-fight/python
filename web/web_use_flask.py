from flask import Flask
from flask import request

app = Flask(__name__)
print(__name__)
print(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Welcome to our Home...</h1>'

@app.route('/signin', methods=['GET'])
def signin_from():
    return '''<form action="/signin" method="post">
    <p><input name="username"></p>
    <p><input name="password" type="password"></p>
    <p><button type="submit">Sign In</button></p>
    </form>'''

@app.route('/signin', methods=['POST'])
def signin():

    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h2>Hello Admin!</h2>'
    return '<h2>Hello %s!</h2>' % request.form['username']

if __name__ == '__main__':
    app.run()
