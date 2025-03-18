from datetime import datetime
from sql_connection import get_sql_connection

def insert_order(connection, order):
    cursor = connection.cursor()

    order_query = ("INSERT INTO ORDERS (customer_name, grand_total, date_time) VALUES (%s, %s, %s)")
    order_data = (order['customer_name'], order['grand_total'], datetime.now())

    cursor.execute(order_query, order_data)
    order_id = cursor.lastrowid

    order_details_query = ("INSERT INTO ORDER_DETAILS (order_id, product_id, quantity, total_price) VALUES (%s, %s, %s, %s)")
    order_details_data = []
    for order_detail_record in order['order_details']:
        order_details_data.append([
            order_id,
            int(order_detail_record['product_id']),
            float(order_detail_record['quantity']),
            float(order_detail_record['total_price'])
        ])
    cursor.executemany(order_details_query, order_details_data)

    connection.commit()

    return order_id

def get_order_details(connection, order_id):
    cursor = connection.cursor()

    query = ("SELECT * FROM order_details WHERE order_id = %s")

    query = ("SELECT od.order_id, od.quantity, od.total_price, p.name, p.price FROM order_details od LEFT JOIN products p on od.product_id = p.product_id where od.order_id = %s")

    data = (order_id, )

    cursor.execute(query, data)

    # total_price = aggregated price, price = price of individual item
    records = []
    for(order_id, quantity, total_price, product_name, price) in cursor:
        records.append({
            'order_id': order_id,
            'quantity': quantity,
            'total_price': total_price,
            'product_name': product_name,
            'price': price
        })

    cursor.close()

    return records

def get_all_orders(connection):
    cursor = connection.cursor()
    query = ("SELECT * FROM orders")
    cursor.execute(query)

    response = []
    for (order_id, customer_name, grand_total, dt) in cursor:
        response.append({
            'order_id': order_id,
            'customer_name': customer_name,
            'grand_total': grand_total,
            'date_time': dt
        })

    cursor.close()

    for record in response:
        record['order_details'] = get_order_details(connection, record['order_id'])

    return response

if __name__ == '__main__':
    connection = get_sql_connection()
    print(insert_order(connection, {
         'customer_name': 'Stanley',
         'grand_total': 130,
         'date_time': datetime.now(),
         'order_details': [
            {
                 'product_id': 3,
                 'quantity': 1,
                 'total_price': 100
           },
            {
                 'product_id': 10,
                 'quantity': 1,
                 'total_price': 30
             }
         ]
    }))