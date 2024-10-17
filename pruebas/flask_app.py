
# A very simple Flask Hello World app for you to get started with...
from flask import Flask, redirect, render_template, request, url_for,flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.exc import IntegrityError
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
"""
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="root",
    password="JILTUB69",
    hostname="127.0.0.1:3306",
    databasename="JIL",
)
if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
"""
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:JILTUB69@127.0.0.1:3306/JIL"
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(app, model_class=Base)
#apellido = db.Column(db.String)
class User(db.Model):
        __tablename__ ="usuario"
        id : Mapped[int] = mapped_column(db.Integer, primary_key=True,autoincrement=True)
        mail : Mapped[str] = mapped_column(db.String,unique=True)
        nombre : Mapped[str] = mapped_column(db.String)
        rol : Mapped[str] = mapped_column(db.String)
        contrasena : Mapped[str] = mapped_column(db.String)
if __name__=="__main__":
    with app.app_context():
        db.create_all()
        #db.session.add(User(mail="example"))
        db.session.commit()
        users = db.session.execute(db.select(User)).scalars()
    app.run(debug=True)
    
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
    
    if request.method == "POST":
        try:
            #user = User(nombre=request.form["nombres"], mail=request.form["correo"], contrasena=request.form["contraseña"],apellido="",rol="al")
            user = User(nombre=request.form["nombres"], mail=request.form["correo"], contrasena=request.form["contraseña"],rol="al")
            print(request.form["nombres"])
            print(request.form["correo"])
            print(request.form["contraseña"])
            # Add the new user to the session and commit to the database
            db.session.add(user)
            db.session.commit()
            flash(f"usuario guardado")
        except IntegrityError as e:
            #esto asugura que la sesión no tenga inconvenientes luego
            db.session.rollback()
            if 'Duplicate entry' in str(e.orig):
                flash(f"Mail duplicado")
            #en caso de que error no cumpla con la duplicación 
            else:
                flash(f"Error al guardar el usuario en la base de datos")
        return render_template("homeInscribirse.html")
    else:
        return render_template('homeInscribirse.html')
    
    

@app.route('/homeIngresar',methods=['GET', 'POST'])
def homeIngresar():
    return render_template('homeIngresar.html')



@app.route('/logout')
def logout():
    return render_template('home.html')

