from flask import Flask, render_template, request


app = Flask(__name__)

"""From this point @app.route signifies adress call that triggers templates"""
@app.route('/')#Defult view of webapp
def index():
    return render_template('index.html')

@app.route('/login')#Login Interface
def login():
    return render_template('loginform.html')

@app.route('/signup')#Login Interface
def signup():
    return render_template('signupform.html')

@app.route('/forgot_password')
def forrgot_password():
    return render_template('forgot_password.html')

@app.route('/aboutme')
def aboutme():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

"""@app.route('/search-request', methods = ['POST'])
def process_place():
    search = request.form['search']
    print("Recieved request to check temp of city '" + search + "'")
    temp = weatherscrape.getdata(str(search))
    return render_template("place.html", search = search, temp = temp)"""

if __name__ == "__main__":
    app.run()
