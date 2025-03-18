from flask import Flask, request, jsonify
import products_dao, orders_dao, unit_dao
from sql_connection import get_sql_connection
import json
from flask import redirect, url_for, render_template
from login import get_login

app = Flask(__name__)

connection = get_sql_connection()

# Read, Add, Delete - Products
@app.route('/getProducts', methods = ['GET'])
def get_products():
    products = products_dao.get_all_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertProduct', methods = ['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    product_id = products_dao.insert_new_products(connection, request_payload)
    response = jsonify({'product_id': product_id})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/deleteProduct', methods = ['POST'])
def delete_product():
    return_id = products_dao.delete_product(connection, request.form['product_id'])
    response = jsonify({'product_id': return_id})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# Read, Add - Orders
@app.route('/getOrders', methods = ['GET'])
def get_orders():
    orders = orders_dao.get_all_orders(connection)
    response = jsonify(orders)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertOrder', methods = ['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    order_id = orders_dao.insert_order(connection, request_payload)
    response = jsonify({'order_id': order_id})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# Read - Unit
@app.route('/getUnit', methods = ['GET'])
def get_unit():
    unit = unit_dao.get_unit(connection)
    response = jsonify(unit)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server for Store Application System")
    app.run(port = 5000)