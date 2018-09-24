from flask import Flask, render_template, request, flash
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
    return render_template('index.html')

@app.route('/login')#Login Interface
def login():
    return render_template('loginform.html')

@app.route('/signup', methods=['GET', 'POST'])#Login Interface
def signup():
    form = ReusableForm(request.form)
    if request.method == 'POST':
        
        firstname=request.form['firstname']
        lastname=request.form['lastname']
        email=request.form['phone']
        password=request.form['password']
        passwordconfirm=request.form['passwordconfirm']
        print(firstname)

        if form.validate() and password == passwordconfirm:
            flash('You have signed up!')
        elif password != passwordconfirm:
            flash('Try Again - Password Didn\'t Match.')
        elif len(password) < 6:
            flash('Try Again - Password Needs To Be Over 6 Characters.')
        else:
            flash('Error: All the form fields are required. ')
    return render_template('signupform.html', form=form)

@app.route('/forgot_password')
def forrgot_password():
    return render_template('forgot_password.html')

@app.route('/aboutme')
def aboutme():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run()
