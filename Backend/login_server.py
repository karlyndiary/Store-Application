from flask import Flask, request, jsonify, redirect, url_for, send_from_directory
import os, logging
from sql_connection import get_sql_connection
from login import get_login

app = Flask(__name__)

# Explicitly set the correct path for the frontend folder
FRONTEND_FOLDER = os.path.abspath(os.path.join(app.root_path, '../frontend'))
    
@app.route('/')
def login():
    return redirect(url_for('login'))

@app.route('/getLogin', methods=['POST'])
def login_route():
    try:
        email = request.form.get('email')
        password = request.form.get('password')

        if not email or not password:
            return jsonify({'error': 'Email and password are required'}), 400

        connection = get_sql_connection()
        try:
            user_details = get_login(connection, {'email': email, 'password': password})
        finally:
            connection.close()  # Ensure connection closure

        if not user_details or password not in user_details:
            return jsonify({'error': 'Invalid email or password'}), 401

        stored_password = user_details['password']

        if stored_password != password:
            return jsonify({'error': 'Invalid Password'}), 401
        
        # returns the user to index.html if login is successful
        return send_from_directory(FRONTEND_FOLDER, 'index.html')

    except Exception as e:
        logging.error(f"Error: {str(e)}", exc_info=True)
        return jsonify({'error': 'An Internal error occurred'}), 500


if __name__ == "__main__":
    print("Starting Python Flask Server for Store Application System")
    app.run(port=5000)
