from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET','POST'])
def validation():

	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		verify = request.form['verify']
		email = request.form['email']
		print(username)
		print(password)
		print(verify)
		print(email)


		user_error = ''
		password_error = ''
		verify_error = ''
		email_error = ''

		if len(username) < 3 or len(username) > 20 or " " in username:
			user_error = 'Invalid User Name'
		
		if len(password) < 3 or len(password) > 20 or " " in password:
			password_error = 'That is not a valid password'
		
		if verify != password:
			verify_error = 'Passwords do not match'
		
		if email and (len(email) < 3 or len(email) > 20 or " " in email or email.count("@") != 1 or email.count(".") != 1):
			email_error = 'That is not a vailid email'
		
		elif not user_error and not password_error and not verify_error and not email_error:
			return redirect('/welcome?username='+username)

		password = ''
		verify = ''
		return render_template('index.html', username=username, password=password, verify=verify, email=email,user_error=user_error,
		password_error=password_error, verify_error=verify_error, email_error=email_error)
	else: 
		return render_template('index.html')

@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html',username=username)


app.run()