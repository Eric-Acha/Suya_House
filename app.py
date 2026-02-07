# app.py

from flask import Flask, request, render_template, redirect
import mysql.connector
import json

app = Flask(__name__)


# MySQL Configuration
conn = mysql.connector.connect(
    host="localhost",

    user="root",
    password="EmmamyAngel04",
    database="suya_house"
)
cursor = conn.cursor()


@app.route('/')
def home():
    return render_template('suya.html')


@app.route('/submit_order', methods=['POST'])
def submit_order():
    name = request.form['name']
    email = request.form['email']
    order_data = json.loads(request.form['order_data'])

    cursor.execute(
        "INSERT INTO orders (customer_name, customer_email) VALUES (%s, %s)", (name, email))
    order_id = cursor.lastrowid

    for item in order_data:
        cursor.execute("""
            INSERT INTO order_items (order_id, item_id, item_name, quantity, price)
            VALUES (%s, %s, %s, %s, %s)
        """, (order_id, item['id'], item['name'], item['qty'], item['price']))

    conn.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
