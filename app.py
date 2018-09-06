from flask import Flask, render_template, request
import database_backend

app = Flask(__name__)

"""From this point @app.route signifies adress call that triggers templates"""
@app.route('/')#Defult view of webapp
def index():
    return render_template('index.html')

@app.route('/temperature')#Search interface, same elmeents used on search-result
def temperature():
    return render_template('temperature.html')

@app.route('/googlemaps')
def googlemaps():
    return render_template('index.html')

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
    app.run(debug=True)
