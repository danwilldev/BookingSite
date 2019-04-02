from flask import Flask, render_template, request, flash, redirect, url_for
from userdatabase import Database #Custom Database Script
from classdatabase import ClassDatabase
from flask_wtf import Form
from wtforms import Form, StringField, PasswordField, BooleanField, SubmitField, TextField, validators
from wtforms.validators import DataRequired
from flask_login import LoginManager, current_user, login_user, logout_user, login_required, UserMixin

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'REPLACEWITHSECUREKEYDAN'

###Login###
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = ''

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

class User(UserMixin):
  def __init__(self,id):
    self.id = id
    


class ReusableForm(Form):
    firstname = TextField('firstname:', validators=[validators.required()])
    lastname = TextField('lastname:', validators=[validators.required()])
    phone = TextField('phone:', validators=[validators.required()])
    password = PasswordField('password:', validators=[validators.required(), validators.Length(min=6)])
    passwordconfirm = PasswordField('passwordconfirm:', validators=[validators.required(), validators.Length(min=6)])

class ReusableClassForm(Form):
    day = TextField('day:', validators=[validators.required()])
    name = TextField('name:', validators=[validators.required()])
    time = TextField('time:', validators=[validators.required()])
    location = PasswordField('location:', validators=[validators.required()])
    

"""From this point @app.route signifies adress call that triggers templates"""
@app.route('/')#Defult view of webapp
def index():
    details = ClassDatabase.classdetails()
    if current_user.is_active == True:
        return render_template('index.html', loggedin = 1, details = details)
    else:
        return render_template('index.html', loggedin = 0, details = details)

@app.route('/login', methods=['GET', 'POST'])#Login Interface
def login():
    form = ReusableForm(request.form)
    if request.method == 'POST':

        email=request.form['email']
        password=request.form['password']

        if Database.check(email, password) == True:
            login_user(User(email))
            return render_template('index.html', loggedin = 1)
            #return redirect(url_for('index', loggedin= 1))
        else:
            flash('User Not Found.')

    return render_template('loginform.html', form=form, loggedin = 0)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

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
            flash('You have signed up! Now Login')
            db = Database(email, firstname, lastname, phone , password)
            #db.create()
            db.hashpw()
            db.add()
        
        else:
            flash('Error: Something went wrong there, inform Dan.')
    return render_template('signupform.html', form=form)

@app.route('/forgot_password', methods=['GET', 'POST'])
def forrgot_password():
    return render_template('forgot_password.html')

@app.route('/account')
@login_required
def account():
    uuid = Database.uuid(current_user.get_id())
    details = Database.userdetails(uuid)
    firstname = details[0]
    lastname = details[1]
    phone = details[2]
    return render_template('account.html', email = current_user.get_id(), firstname = firstname, lastname = lastname, phone = phone, loggedin = 1)
    #return current_user.get_id()

@app.route('/about')
def aboutme():
    if current_user.is_active == True:
        return render_template('about.html', loggedin = 1)
    else:
        return render_template('about.html', loggedin = 0)

@app.route('/admin', methods=['GET', 'POST'])
#@login_required
def admin():
    details = ClassDatabase.classdetails()
    length = len(details)
    l = []
    for x in details[0]:
        l.append(x)
    
    return render_template('admin.html', loggedin = 1, details = details, length = length)

@app.route('/admin/add', methods=['GET', 'POST'])
#@login_required
def adminadd():
    form = ReusableClassForm(request.form)
    if request.method == 'POST':
        day=request.form['day']
        name=request.form['name']
        time=request.form['time']
        location=request.form['location']
        db = ClassDatabase(day,name,time,location)
        db.add()
    return render_template('adminadd.html', loggedin = 1, form = form)



@app.route('/location')
def location():
    if current_user.is_active == True:
        return render_template('googlemaps.html', loggedin = 1)
    else:
        return render_template('googlemaps.html', loggedin = 0)

if __name__ == "__main__":
    app.run()
