from flask import Flask, render_template, session, redirect, url_for, request
import mysql.connector

server = Flask(__name__, template_folder='templates', static_folder='static')
# app = Dash(__name__, server=server, url_base_pathname='/test/')
# app.layout = html.Div([html.H1('This Is head',style={'textAlign':'center'})])

server.secret_key = 'mysecret'

mydb = mysql.connector.connect(
  host='rental-data.cckjcfdnzspp.ap-southeast-2.rds.amazonaws.com',
  user='asur0015',
  password='finalsemproject'
)

mycursor = mydb.cursor()
mycursor.execute("select * from rental_data.rental limit 10;")
myresult = mycursor.fetchall()

@server.route('/')
def home():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    return render_template('home.html')

@server.route('/suburb/forecast')
def suburb_forecast():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    return render_template('suburb_forecast.html')

@server.route('/suburb/<int:Number>')
def suburb_historicaldata(Number):
    if 'logged_in' not in session:
        return redirect(url_for('login'))

    if Number < 1 or Number > 7:
        return redirect(url_for('home'))
    else:
        return render_template('historical_trends/subdat'+str(Number)+'.html')

@server.route('/login', methods=['GET', 'POST'])
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

# @server.route("/dash")
# def MyDashApp():
#     return app.index()

if __name__ == '__main__':
    server.run_server(debug=True)