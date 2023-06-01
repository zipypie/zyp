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
  
  
#GET method for customer
@app.route("/customers", methods=["GET"])
def get_customers():
    format = request.args.get("format", "").lower()
    cur = mysql.connection.cursor()
    query = """
    SELECT * FROM customer
    """
    cur.execute(query)
    data = cur.fetchall()
    cur.close()

    if format == "xml":
        # Convert data to XML format
        root = ET.Element("customers")
        for row in data:
            customer = ET.SubElement(root, "customer")
            for key, value in row.items():
                field = ET.SubElement(customer, key)
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
      
@app.route("/atm", methods=["GET"])
def get_atm():
    format = request.args.get("format", "").lower()
    cur = mysql.connection.cursor()
    query = """
    SELECT * FROM atm
    """
    cur.execute(query)
    data = cur.fetchall()
    cur.close()

    if format == "xml":
        # Convert data to XML format
        root = ET.Element("atm")
        for row in data:
            atm = ET.SubElement(root, "atm")
            for key, value in row.items():
                field = ET.SubElement(atm, key)
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
      
@app.route("/phone", methods=["GET"])
def get_phone():
    format = request.args.get("format", "").lower()
    cur = mysql.connection.cursor()
    query = """
    SELECT * FROM phone
    """
    cur.execute(query)
    data = cur.fetchall()
    cur.close()

    if format == "xml":
        # Convert data to XML format
        root = ET.Element("phone")
        for row in data:
            phone = ET.SubElement(root, "phone")
            for key, value in row.items():
                field = ET.SubElement(phone, key)
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
      

if __name__ == "__main__":
    app.run(debug=True)
