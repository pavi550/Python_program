# Mysql demo

import os
import MySQLdb.connections

# Create the connection object

db_name = input('Enter the database name : ' )
myconn = mysql.connector.connect(host="localhost", user="root", passwd="namish", database=db_name)