from flask import Flask, render_template, request, flash, redirect, url_for
from database import Database #Custom Database Script
from flask_wtf import Form
from wtforms import Form, StringField, PasswordField, BooleanField, SubmitField, TextField, validators
from wtforms.validators import DataRequired

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'REPLACEWITHSECUREKEYDAN'

class ReusableForm(Form):
    firstname = TextField('firstname:', validators=[validators.required()])
    lastname = TextField('lastname:', validators=[validators.required()])
    phone = TextField('phone:', validators=[validators.required()])
    password = PasswordField('password:', validators=[validators.required(), validators.Length(min=6)])
    passwordconfirm = PasswordField('passwordconfirm:', validators=[validators.required(), validators.Length(min=6)])

"""From this point @app.route signifies adress call that triggers templates"""
@app.route('/')#Defult view of webapp
def index():
    title = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return render_template('index.html', title = title)

@app.route('/login', methods=['GET', 'POST'])#Login Interface
def login():
    form = ReusableForm(request.form)
    if request.method == 'POST':
        email=request.form['email']
        password=request.form['password']

        if Database.check(email, password) == True:
            return redirect(url_for('index', loggedin= 1))
        else:
            flash('User Not Found.')

    return render_template('loginform.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])#Sign Up Interface
def signup():
    form = ReusableForm(request.form)
    if request.method == 'POST':
        count = []
        firstname=request.form['firstname']
        lastname=request.form['lastname']
        email=request.form['email']
        phone=request.form['phone']
        password=request.form['password']
        passwordconfirm=request.form['passwordconfirm']
        count.extend([firstname, lastname, email, phone, password, passwordconfirm])
        total = 0
        for x in count:
            x = x
            total = total + 1
        if total != 6:
            flash('Error: Please fill out all details.')
        elif password != passwordconfirm:
            flash('Try Again - Password Didn\'t Match.')
        elif len(password) < 6:
            flash('Try Again - Password Needs To Be Over 6 Characters.')
        elif form.validate():
            flash('You have signed up!')
            db = Database(email, firstname, lastname, phone , password)
            db.create()
            db.hashpw()
            db.add()
        
        else:
            flash('Error: Something went wrong there, inform Dan.')
    return render_template('signupform.html', form=form)

@app.route('/forgot_password', methods=['GET', 'POST'])
def forrgot_password():
    return render_template('forgot_password.html')

@app.route('/about')
def aboutme():
    return render_template('about.html')

@app.route('/location')
def contact():
    return render_template('googlemaps.html')

if __name__ == "__main__":
    app.run()
