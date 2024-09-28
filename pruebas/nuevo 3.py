
# A very simple Flask Hello World app for you to get started with...
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

picFolder= os.path.join("static","pics")
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config["DEBUG"] = True
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="IvanGarcia564846",
    password="-)WA4UhsiNRL_zv",
    hostname="IvanGarcia56484651.mysql.pythonanywhere-services.com",
    databasename="IvanGarcia564846$JIL",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

""" class Comment(db.Model):

    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))
"""
class User(db.Model):
        __tablename__ ="Usuarios"
        mail = db.Column(db.String(4096),primary_key=True)
        nombre = db.Column(db.String(4096))
        apellido = db.Column(db.String(4096))
        rol=db.Column(db.String(4096))
        contrasena=db.Column(db.String(4096))

"""
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("main_page.html", comments=Comment.query.all())
    comment = Comment(content=request.form["contents"])
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('index'))
"""
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/homeInscribirse',methods=['GET', 'POST'])
def homeInscribirse():
    return render_template('homeInscribirse.html')
    if request.method == "GET":
        return render_template("main_page.html", comments=User.query.all())

    # Assuming your User model has fields `nombres`, `correo`, and `contraseña`
    user = User(nombre=request.form["nombres"], mail=request.form["correo"], contrasena=request.form["contraseña"],apellido="",rol="al")

    # Add the new user to the session and commit to the database
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('homeInscribirse'))

@app.route('/homeIngresar',methods=['GET', 'POST'])
def homeIngresar():
    return render_template('homeIngresar.html')
    if request.method == 'POST':
        User(request.form.get('correo'), request.form.get('contraseña'))
        print (User.nombres)
    else:
        return homeInscribirse()



@app.route('/logout')
def logout():
    return render_template('home.html')

