from flask import Flask, make_response, jsonify, request
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config["MYSQL_HOST"]= "localhost"
app.config["MYSQL_USER"]= "root"
app.config["MYSQL_PASS"]= ""
app.config["MYSQL_DB"]="mobile_purchases_db"

app.config["MYSQL_CURSOSCLASS"]= "DictCursor"

mysql = MySQL(app)

@app.route("/")
def hello_world():
    return "<p>Hello World</p>"

@app.route("/customers",methods=["GET"])
def get_customers():
  cur = mysql.connection.cursor()
  query="""
  select * from customer
  """
  cur.execute(query)
  data = cur.fetchall()
  cur.close()
  return make_response(jsonify(data),200)

if __name__ == "__main__":
    app.run(debug=True)