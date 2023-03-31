from flask import Flask
import mysql.connector
from dash import Dash, html, dcc

app = Flask(__name__, template_folder='templates', static_folder='static')

mydb = mysql.connector.connect(
  host='rental-data.cckjcfdnzspp.ap-southeast-2.rds.amazonaws.com',
  user='asur0015',
  password='finalsemproject'
)

mycursor = mydb.cursor()
mycursor.execute("select * from rental_data.rental limit 10;")
myresult = mycursor.fetchall()

appDash = Dash(__name__,server=app,url_base_pathname='/dash/')

appDash.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

])

@app.route('/')
def home():

    total = []

    for item in myresult:
        total.append(str(item[0])+" "+str(item[1])+" "+str(item[2])+" "+str(item[3])+" "+str(item[4])+" "+str(item[5])+" "+str(item[6]))
    
    total = ''.join(total)

    return total

@app.route('/dash')
def dashHome():

    return appDash.index()


if __name__ == '__main__':
    app.run()