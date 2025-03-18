from flask import Flask
from sql_connection import get_sql_connection

app = Flask(__name__)

def get_login(connection, credentials):

    cursor = connection.cursor()

    query = ("SELECT user_id, email, password FROM users WHERE email = %s AND password = %s")

    cursor.execute(query, (credentials['email'], credentials['password']))

    user = cursor.fetchone()  # Fetch the first match

    if user: 
        user_id, email, password = user
        return{
            'user_id': user_id,
            'email': email,
            'password': password,
        }
    
    return None  # Return None if no user is found

if __name__ == "__main__":
    connection = get_sql_connection()

    # Example credentials for testing
    credentials = {
        "email": "mia@gmail.com",
        "password": "1234"
    }
    
    result = get_login(connection, credentials)

    if result:
        print(f"Login successful: {result}")
    else:
        print("Invalid username or password.")
