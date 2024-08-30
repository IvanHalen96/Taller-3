
from flask import Flask, render_template, url_for, flash, redirect



app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
@app.route("/")
def index():
    return render_template('home.html')

@app.route("/home_registered")
def home():
    return render_template('home_registered.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('home.html')

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/profile")
def profile():
    return "<p>Hello, World!</p>"

@app.route("/offerlist")
def offerlist():
    return "<p>Hello, World!</p>"

@app.route("/paymethod")
def paymethod():
    return "<p>Hello, World!</p>"
#ENTRAR AL CURSO COMPRADO, VER MATERIAS, MATERIAL DE LAS CLASES Y AVANCES
#examen de lo aprendido (forms o cuestionario estilo linkedin)


# A very simple Flask Hello World app for you to get started with...

from flask import Flask, url_for, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route('/')
def index():
    return render_template('home.html')


@app.route("/home_registered")
def home():
    return render_template('home_registered.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('home.html')

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/profile")
def profile():
    return "<p>Hello, World!</p>"

@app.route("/offerlist")
def offerlist():
    return "<p>Hello, World!</p>"

@app.route("/paymethod")
def paymethod():
    return "<p>Hello, World!</p>"

