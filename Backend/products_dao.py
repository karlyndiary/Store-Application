from sql_connection import get_sql_connection

def get_all_products(connection):

    cursor = connection.cursor()

    query = ("SELECT p.product_id, p.name, p.unit_id, p.price, u.unit_name FROM store.products p INNER JOIN store.unit u ON p.unit_id = u.unit_id")

    cursor.execute(query)

    response = []

    for(product_id, name, unit_id, price, unit_name) in cursor:
        response.append(
            {
                'product_id': product_id,
                'name': name,
                'unit_id': unit_id,
                'price': price,
                'unit_name': unit_name
            }
        )

    return response

def insert_new_products(connection, products):

    cursor = connection.cursor()

    query = ("INSERT INTO products "
               "(name, unit_id, price) "
               "VALUES (%s, %s, %s)")
    data = (products['product_name'], products['unit_id'], products['price'])
    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id):

    cursor = connection.cursor()

    query = ("DELETE FROM products WHERE product_id=" + str(product_id))

    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid

if __name__ == '__main__':
    connection = get_sql_connection()
    print(delete_product(connection, 7))