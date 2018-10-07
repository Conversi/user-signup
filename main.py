from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

def username():
    user = request.form['username']
    if len(user) < 3 or len(user) > 20 or " " in user:
        return render_template('index.html', username=username)

def password():
    pasw = request.form['password']
    if len(pasw) < 3 or len(pasw) > 20 or " " in pasw:
        return "That is not a valid password"

def verify():
    pasw = request.form['password']
    veri = request.form['verify_password']
    if veri != pasw:
        return "Passwords don't match"

def email():
    emai = request.form['email']
    if len(emai) < 3 or len(emai) > 20 or  " " in emai or emai.count("@") != 1 or emai.count(".") != 1:
        return "That's not a valid email"

@app.route("/welcome", methods=['POST'])
def welcome():
    user_name = request.form['username']
    return render_template('welcome.html', username = user_name)

@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template('index.html')

app.run()