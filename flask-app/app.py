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


# @app.route('/')
# def homeTest():

#     total = []

#     for item in myresult:
#         total.append(str(item[0])+" "+str(item[1])+" "+str(item[2])+" "+str(item[3])+" "+str(item[4])+" "+str(item[5])+" "+str(item[6]))
    
#     total = ''.join(total)

#     return render_template('home.html')

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run()