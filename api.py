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


@app.route("/customers", methods=["GET"])
def get_all_customers():
    return fetch_data_from_table("customer")


@app.route("/customers/<int:customer_id>", methods=["GET"])
def get_customer(customer_id):
    return fetch_data_from_table("customer", customer_id)


@app.route("/atms", methods=["GET"])
def get_all_atms():
    return fetch_data_from_table("atm")


@app.route("/atms/<int:atm_id>", methods=["GET"])
def get_atm(atm_id):
    return fetch_data_from_table("atm", atm_id)


@app.route("/phones", methods=["GET"])
def get_all_phones():
    return fetch_data_from_table("phone")


@app.route("/phones/<int:phone_id>", methods=["GET"])
def get_phone(phone_id):
    return fetch_data_from_table("phone", phone_id)


@app.route("/products", methods=["GET"])
def get_all_products():
    return fetch_data_from_table("product")


@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    return fetch_data_from_table("product", product_id)


@app.route("/product_prices", methods=["GET"])
def get_all_product_prices():
    return fetch_data_from_table("product_price")


@app.route("/product_prices/<int:product_price_id>", methods=["GET"])
def get_product_price(product_price_id):
    return fetch_data_from_table("product_price", product_price_id)


@app.route("/payments", methods=["GET"])
def get_all_payments():
    return fetch_data_from_table("payment")


@app.route("/payments/<int:payment_id>", methods=["GET"])
def get_payment(payment_id):
    return fetch_data_from_table("payment", payment_id)


#POST METHODS
@app.route("/customers", methods=["POST"])
def add_customer():
    cur = mysql.connection.cursor()
    info = request.get_json()
    first_name = info["first_name"]
    last_name = info["last_name"]
    customer_address = info["customer_address"]
    cur.execute(
        """INSERT INTO CUSTOMER(first_name, last_name, customer_address) 
        VALUES (%s, %s, %s)""",
        (first_name, last_name, customer_address),
    )
    mysql.connection.commit()
    print("row(s) affected: {}".format(cur.rowcount))
    rows_affected = cur.rowcount
    cur.close()
    return make_response(jsonify({"message": "added successfully", "rows_affected": rows_affected}), 201)


@app.route("/new_atms", methods=["POST"])
def add_new_atm():
    cur = mysql.connection.cursor()
    info = request.get_json()
    atm_number = info["atm_number"]
    customer_id= info["customer_id"]

    cur.execute(
        """INSERT INTO atm (atm_name, customer_id) 
        VALUES (%s, %s)""",
        (atm_number, customer_id),
    )
    
    mysql.connection.commit()
    print("row(s) affected: {}".format(cur.rowcount))
    rows_affected = cur.rowcount
    cur.close()
    return make_response(jsonify({"message": "added successfully", "rows_affected": rows_affected}), 201)


@app.route("/new_phones", methods=["POST"])
def add_new_phone():
    cur = mysql.connection.cursor()
    info = request.get_json()
    smartphone_number = info["smartphone_number"]
    customer_id = info["customer_id"]

    cur.execute(
        """INSERT INTO phone (smartphone_number, customer_id) 
        VALUES (%s, %s)""",
        (smartphone_number, customer_id),
    )
    mysql.connection.commit()
    print("row(s) affected: {}".format(cur.rowcount))
    rows_affected = cur.rowcount
    cur.close()
    return make_response(jsonify({"message": "added successfully", "rows_affected": rows_affected}), 201)


@app.route("/new_products", methods=["POST"])
def add_new_product():
    cur = mysql.connection.cursor()
    info = request.get_json()
    product_name = info["product_name"]
    product_quantity = info["product_quantity"]

    cur.execute(
        """INSERT INTO product (product_name, product_quantity) 
        VALUES (%s, %s)""",
        (product_name, product_quantity),
    )
    
    mysql.connection.commit()
    print("row(s) affected: {}".format(cur.rowcount))
    rows_affected = cur.rowcount
    cur.close()
    return make_response(jsonify({"message": "added successfully", "rows_affected": rows_affected}), 201)


@app.route("/new_product_prices", methods=["POST"])
def add_new_product_price():
    cur = mysql.connection.cursor()
    info = request.get_json()
    product_id = info["product_id"]
    product_price = info["product_price"]
    
    cur.execute(
        """INSERT INTO product_price (product_id, product_price) 
        VALUES (%s, %s)""",
        (product_id, product_price),
    )
    
    mysql.connection.commit()
    print("row(s) affected: {}".format(cur.rowcount))
    rows_affected = cur.rowcount
    cur.close()
    return make_response(jsonify({"message": "added successfully", "rows_affected": rows_affected}), 201)






#PUT METHODS
@app.route("/update_customers/<int:customer_id>", methods=["PUT"])
def update_customers(customer_id):
    cur = mysql.connection.cursor()
    info = request.get_json()
    first_name = info["first_name"]
    last_name = info["last_name"]
    customer_address = info["customer_address"]
    cur.execute(
        """
        UPDATE customer SET first_name = %s, last_name = %s, customer_address = %s WHERE customer_id = %s
        """,
        (first_name, last_name, customer_address, customer_id),
    )
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()
    return make_response(
        jsonify(
            {"message": "customer updated successfully", "rows_affected": rows_affected}
        ),
        200,
    )


@app.route("/new_atms", methods=["PUT"])
def add_new_atm():
    cur = mysql.connection.cursor()
    info = request.get_json()
    atm_number = info["atm_number"]
    customer_id = info["customer_id"]

    cur.execute(
        """UPDATE atm SET atm_name = %s WHERE customer_id = %s""",
        (atm_number, customer_id),
    )
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()
    return make_response(jsonify({"message": "updated successfully", "rows_affected": rows_affected}), 200)


@app.route("/new_phones", methods=["PUT"])
def add_new_phone():
    cur = mysql.connection.cursor()
    info = request.get_json()
    smartphone_number = info["smartphone_number"]
    customer_id = info["customer_id"]

    cur.execute(
        """UPDATE phone SET smartphone_number = %s WHERE customer_id = %s""",
        (smartphone_number, customer_id),
    )
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()
    return make_response(jsonify({"message": "updated successfully", "rows_affected": rows_affected}), 200)


@app.route("/new_products", methods=["PUT"])
def add_new_product():
    cur = mysql.connection.cursor()
    info = request.get_json()
    product_id = info["product_id"]
    product_quantity = info["product_quantity"]

    cur.execute(
        """UPDATE product SET product_quantity = %s WHERE product_id = %s""",
        (product_quantity, product_id),
    )
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()
    return make_response(jsonify({"message": "updated successfully", "rows_affected": rows_affected}), 200)


@app.route("/new_product_prices", methods=["PUT"])
def add_new_product_price():
    cur = mysql.connection.cursor()
    info = request.get_json()
    product_id = info["product_id"]
    product_price = info["product_price"]

    cur.execute(
        """UPDATE product_price SET product_price = %s WHERE product_id = %s""",
        (product_price, product_id),
    )
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()
    return make_response(jsonify({"message": "updated successfully", "rows_affected": rows_affected}), 200)


@app.route("/customers/<int:customer_id>", methods=["DELETE"])
def delete_customer(customer_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM customer WHERE customer_id = %s", (customer_id,))
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()
    return make_response(jsonify({"message": "deleted successfully", "rows_affected": rows_affected}), 200)


if __name__ == "__main__":
    app.run(debug=True)
