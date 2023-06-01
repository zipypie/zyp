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

def fetch_data_from_table(table_name):
    format = request.args.get("format", "").lower()
    cur = mysql.connection.cursor()
    query = f"SELECT * FROM {table_name}"
    cur.execute(query)
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

@app.route("/customers", methods=["GET"])
def get_customers():
    return fetch_data_from_table("customer")

@app.route("/atms", methods=["GET"])
def get_atm():
    return fetch_data_from_table("atm")

@app.route("/phones", methods=["GET"])
def get_phone():
    return fetch_data_from_table("phone")

@app.route("/products", methods=["GET"])
def get_products():
    return fetch_data_from_table("product")

@app.route("/product_price", methods=["GET"])
def get_product_price():
    return fetch_data_from_table("product_price")

@app.route("/payments", methods=["GET"])
def get_payments():
    return fetch_data_from_table("payments")

if __name__ == "__main__":
    app.run(debug=True)
