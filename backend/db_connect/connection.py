import mysql.connector
from mysql.connector import Error

from db_config import DB_Config

connection = ""
cursor = ""

class DB_CONNECT:
  def connect():
    global connection
    global cursor

    try:
      connection = mysql.connector.connect(host=DB_Config.db_host,
                                          database=DB_Config.db_name,
                                          user=DB_Config.db_username,
                                          password=DB_Config.db_password)
      if connection.is_connected():
        # print("Connected to MySQL Server version")
        cursor = connection.cursor(dictionary=True)

    except Error as e:
      print("Error while connecting to MySQL", str(e))
  
  def disconnect():
    global connection
    global cursor

    try:
      if connection.is_connected():
        cursor.close()
        connection.close()
        # print ("Close mysql connection")
    except Error as e:
      print ("Error while closing mysql", str(e))
  
  def get_connection():
    global connection
    return connection
  
  def get_cursor():
    global cursor
    return cursor

