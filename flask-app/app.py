from flask import Flask, render_template, session, redirect, url_for, request
import mysql.connector

app = Flask(__name__, template_folder='templates', static_folder='static')

app.secret_key = 'mysecret'

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
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    return render_template('home.html')

@app.route('/suburb/forecast')
def suburb_forecast():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    return render_template('suburb_forecast.html')

@app.route('/suburb/historicaldata')
def suburb_historicaldata():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    return render_template('suburb_historicaldata.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Check the login credentials
        if request.form['username'] == 'notsoeasytoguess' and request.form['password'] == 'notsoeasytoguess':
            # Save the login status in the session
            session['logged_in'] = True
            return redirect(url_for('home'))
    
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
    '''

if __name__ == '__main__':
    app.run()