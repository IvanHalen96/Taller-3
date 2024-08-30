

from flask import Flask, url_for, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template('register.html')

@app.route('/logout')
def logout():
    return render_template('home.html')

