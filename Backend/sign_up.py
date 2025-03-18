from flask import Flask, render_template, request, redirect, url_for, session
from sql_connection import get_sql_connection

app = Flask(__name__)

connection = get_sql_connection()

@app.route('/')
def home():
    if 'user_name' in session:
        return render_template('home.html', username = session['user_name'])
    else: 
        return render_template('home.html')

@app.route('/login')
def login():
    if request.method == 'POST':
        user_name = request.form['username']
        password = request.form['password']
        cursor = get_sql_connection.cursor()
        cursor.execute(f"SELECT user_name, password FROM users WHERE user_name = {'user_name'}")
        user = cursor.fetchone()
        cursor.close()
        if user and password == user[1]:
            session['user_name'] = user[0]
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error = 'Invalid username or password')
        
    return render_template('login.html')

if __name__ == "__main__":
    print("Starting Python Flask Server for Store Application System")
    app.run(port = 5000)