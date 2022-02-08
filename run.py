from flask import Flask, render_template,redirect,request,url_for,session
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms .validators import InputRequired,Length,ValidationError


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="postgresql+psycopg2://moringa:Access@localhost/tracy"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.secret_key="Access"
__tablename__="users"
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)


class user(db.Model,UserMixin):
 id=db.Column(db.Integer,primary_key=True)
 firstname=db.Column(db.String(50),nullable=False)
 middlename=db.Column(db.String(50),nullable=False)
 username=db.Column(db.String(50),nullable=False,unique=True)
 email=db.Column(db.String(50),nullable=False,unique=True)
 password=db.Column(db.String(50),nullable=False)
 
 
 class registerForm():
     firstname=StringField(validators=[InputRequired(),Length(min=4,max=20)])
     middlename=StringField(validators=[InputRequired(),Length(min=4,max=20)])
     username=StringField(validators=[InputRequired(),Length(min=4,max=20)])
     email=StringField(validators=[InputRequired(),Length(min=4,max=20)])
     password=StringField(validators=[InputRequired(),Length(min=4,max=20)])
     
     
     def validate_email(self, email):
         existing_user_email=user.query.filter(email=email.data).first()
         if existing_user_email:
             raise ValidationError("The email is already in use!")
         
 class loginForm():
     username=StringField(validators=[InputRequired(),Length(min=4,max=20)])
     email=StringField(validators=[InputRequired(),Length(min=4,max=20)])
     password=StringField(validators=[InputRequired(),Length(min=4,max=20)])
     
     
         
        

@app.route('/home')
def home():
     return render_template('home.html')
 



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login.html')
def login():
    return render_template('login.html')


@app.route('/signup.html')
def signup():
    return render_template('signup.html')


@app.route('/pitch.html')
def count():
    return render_template('pitch.html')



@app.route('/logout.html')
def logout():
    return render_template('logout.html')



@app.route('/contact')
def contactme():
    return render_template('contactme.html')





if __name__ == '__main__':
    app.run(debug=True)
