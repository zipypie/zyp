from flask import Flask, make_response, jsonify, request
from flask_mysqldb import MySQL
import xml.etree.ElementTree as ET

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASS"] = ""
app.config["MYSQL_DB"] = "mobile_purchases_db"
app.config["MYSQL_CURSOSCLASS"] = "DictCursor"

mysql = MySQL(app)

@app.route("/")
def hello_world():
    return "<p>Hello World</p>"

def fetch_data_from_table(table_name, primary_key=None):
    format = request.args.get("format", "").lower()
    cur = mysql.connection.cursor()

    if primary_key is None:
        query = f"SELECT * FROM {table_name}"
        cur.execute(query)
    else:
        key_column = f"{table_name}_id"  # Get the custom key column name based on table_name
        query = f"SELECT * FROM {table_name} WHERE {key_column} = %s"
        cur.execute(query, (primary_key,))  # Pass primary key as a tuple

    columns = [desc[0] for desc in cur.description]  # Get column names
    data = [dict(zip(columns, row)) for row in cur.fetchall()]  # Convert rows to dictionaries
    cur.close()

    if format == "xml":
        # Convert data to XML format
        root = ET.Element(table_name)
        for row in data:
            element = ET.SubElement(root, table_name[:-1])  # Remove 's' from table_name for tag name
            for key, value in row.items():
                field = ET.SubElement(element, key)
                field.text = str(value)

        # Convert XML to string
        xml_data = ET.tostring(root, encoding="utf-8")

        # Set the Content-Type header to indicate XML format
        headers = {"Content-Type": "application/xml"}

        # Return the XML response
        return make_response(xml_data, 200, headers)
    else:
        # Return the JSON response
        return make_response(jsonify(data), 200)

@app.route("/customers/<customer_id>", methods=["GET"])
def get_customers(customer_id):
    return fetch_data_from_table("customer", customer_id)

@app.route("/atm/<atm_id>", methods=["GET"])
def get_atm(atm_id):
    return fetch_data_from_table("atm", atm_id)

@app.route("/phone/<phone_id>", methods=["GET"])
def get_phone(phone_id):
    return fetch_data_from_table("phone", phone_id)

@app.route("/products/<product_id>", methods=["GET"])
def get_products(product_id):
    return fetch_data_from_table("product", product_id)

@app.route("/product_prices/<product_price_id>", methods=["GET"])
def get_product_price(product_price_id):
    return fetch_data_from_table("product_price", product_price_id)

@app.route("/payments/<payment_id>", methods=["GET"])
def get_payment(payment_id):
    return fetch_data_from_table("payment", payment_id)

if __name__ == "__main__":
    app.run(debug=True)
