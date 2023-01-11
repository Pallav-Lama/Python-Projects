from datetime import date
from flask import Flask, render_template, request
import pymysql
pymysql.install_as_MySQLdb()
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/myfirstblog'
db = SQLAlchemy(app)
''' s.n. name email_address phone_number message date'''
class Contact(db.Model):
    sn = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email_address = db.Column(db.String(50), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    message = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(20), nullable=True)
   


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/samplepost")
def samplepost():
    return render_template("post.html")

@app.route("/contact", methods = ["GET", "POST"])
def contact():
    if (request.method == "POST"):
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")

        entry = Contact(name = name, email_address = email, phone_number = phone, date = datetime.now(),  message =message)
        db.session.add(entry)
        db.session.commit()

    return render_template("contact.html")


app.run(debug= True)