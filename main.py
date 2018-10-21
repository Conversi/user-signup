from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/index", methods=['POST'])
def validation():

        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']
        email = request.form['email']

        user_error = ''
        password_error = ''
        verify_error = ''
        email_error = ''

        if len(username) < 3 or len(username) > 20 or " " in username:
                user_error = 'Invalid User Name'

        elif len(password) < 3 or len(password) > 20 or " " in password:
                password_error = 'That is not a valid password'
                password = ''

        elif verify != password:
                verify_error = 'Passwords do not match'
                verify = ''

        elif len(email) < 3 or len(email) > 20 or  " " in email or email.count("@") != 1 or email.count(".") != 1:
                email_error = 'That is not a vailid email'
        
        elif not user_error and not password_error and not verify_error and not email_error:
                return redirect('/welcome')
        else:
                return render_template('index.html', username=username, password=password, verify=verify, email=email,user_error=user_error,
                password_error=password_error, verify_error=verify_error, email_error=email_error)

@app.route("/welcome", methods=['POST'])
def welcome():
    username = request.form['username']
    return render_template('welcome.html', username=username)

@app.route("/")
def display():
    return render_template('index.html')

app.run()