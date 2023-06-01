from flask import Flask, make_response, jsonify, request
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config["MYSQL_HOST"]= "localhost"
app.config["MYSQL_USER"]= "root"
app.config["MYSQL_PASS"]= ""
app.config["MYSQL_DB"]="mobile_purchases_db"
