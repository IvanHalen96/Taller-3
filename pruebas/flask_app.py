
# A very simple Flask Hello World app for you to get started with...
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import os

app = Flask(__name__)
comments = []
picFolder= os.path.join("static","pics")
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config["DEBUG"] = True
"""
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="IvanGarcia564846",
    password="-)WA4UhsiNRL_zv",
    hostname="IvanGarcia56484651.mysql.pythonanywhere-services.com",
    databasename="IvanGarcia564846$JIL",
)"""
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="root",
    password="JILTUB69",
    hostname="127.0.0.1:3306",
    databasename="JIL",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class User(db.Model):
        __tablename__ ="usuario"
        mail = db.Column(db.String(255),primary_key=True)
        nombre = db.Column(db.String(255))
        apellido = db.Column(db.String(255))
        rol=db.Column(db.String(255))
        contrasena=db.Column(db.String(255))

@app.route('/')
def index():
    return render_template('home.html')

@app.route("/main_page", methods=["GET", "POST"])
def main_page():
    if request.method == "GET":
        return render_template("main_page.html", comments=comments)
    comments.append(request.form["contents"])
    return redirect(url_for('index'))

@app.route('/admin')
def admin():
    return render_template('admin.html')
@app.route('/admin2')
def admin2():
    request=User.query.all()
    print(request)
    return render_template('admin.html')
@app.route('/carrera')
def carrera():
    return render_template('carrera.html')
@app.route('/contenidos')
def contenidos():
    return render_template('contenidos.html')
@app.route('/cursosymaterias')
def cursosymaterias():
    return render_template('cursosymaterias.html')
@app.route('/inicio')
def inicio():
    return render_template('inicio.html')
@app.route('/layout')
def layout():
    return render_template('layout.html')
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/aulaAnalisis')
def aulaAnalisis():
    return render_template('aulaAnalisis.html')
@app.route('/aulaVirtualCarreras')
def aulaVirtualCarreras():
    return render_template('aulaVirtualCarreras.html')
@app.route('/boletin')
def boletin():
    return render_template('boletin.html')
@app.route('/contacto')
def contacto():
    return render_template('contacto.html')
@app.route('/homeAlumno')
def homeAlumno():
    return render_template('homeAlumno.html')
@app.route('/infoAnalisis')
def infoAnalisis():
    return render_template('infoAnalisis.html')
@app.route('/inscripciones')
def inscripciones():
    return render_template('inscripciones.html')
@app.route('/inscripcionesMaterias')
def inscripcionesMaterias():
    return render_template('inscripcionesMaterias.html')
@app.route('/tramites')
def tramites():
    return render_template('tramites.html')


@app.route('/homeInscribirse',methods=['GET', 'POST'])
def homeInscribirse():
    return render_template('homeInscribirse.html')
    if request.method == "POST":
        return render_template("homeInscribirse.html", usuario=User.query.all())

    # Assuming your User model has fields `nombres`, `correo`, and `contraseña`
    user = User(nombre=request.form["nombres"], mail=request.form["correo"], contrasena=request.form["contraseña"],apellido="",rol="al")
    print(request.form["nombres"])
    print(request.form["correo"])
    print(request.form["contraseña"])
    # Add the new user to the session and commit to the database
    db.session.add(user)
    db.session.commit()
    return render_template('homeInscribirse.html')

@app.route('/homeIngresar',methods=['GET', 'POST'])
def homeIngresar():
    return render_template('homeIngresar.html')



@app.route('/logout')
def logout():
    return render_template('home.html')

