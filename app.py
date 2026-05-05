from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy credentials
USERNAME = "admin"
PASSWORD = "password"

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USERNAME and password == PASSWORD:
            return redirect(url_for('dashboard'))
        else:
            return "Invalid credentials given ", 401
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return "Welcome to Dashboard!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
