from flask import Flask, render_template
import mysql.connector

app = Flask(__name__, template_folder='templates', static_folder='static')

mydb = mysql.connector.connect(
  host='rental-data.cckjcfdnzspp.ap-southeast-2.rds.amazonaws.com',
  user='asur0015',
  password='finalsemproject'
)

mycursor = mydb.cursor()
mycursor.execute("select * from rental_data.rental limit 10;")
myresult = mycursor.fetchall()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/suburb')
def suburb():
    return render_template('suburb.html')

@app.route('/suburb/forecast')
def suburb_forecast():
    return render_template('suburb_forecast.html')

@app.route('/suburb/historicaldata')
def suburb_historicaldata():
    return render_template('suburb_historicaldata.html')

if __name__ == '__main__':
    app.run()