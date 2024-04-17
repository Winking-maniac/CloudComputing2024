from flask import Flask
#import pymysql
import mysql.connector
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/db")
def db_select_all():
    res = ""
    connection = mysql.connector.connect(
        host="0.0.0.0",
        user='not_root',
        password='qwerty',
        database='db_name',
        auth_plugin='mysql_native_password'
    )
    with connection.cursor() as cursor:
        select_all_rows = "SELECT * FROM `t`"
        cursor.execute(select_all_rows)

        rows = cursor.fetchall()
        for row in rows:
            res += "<p>" + str(row) + "</p>"
    connection.close()
    return res
