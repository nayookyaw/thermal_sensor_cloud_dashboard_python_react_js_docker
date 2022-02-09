from mysql.connector import connection
from db_connect.connection import DB_CONNECT

class Query:
  def selectAll(sql):
    # print ("select all")

    try:

      #connect to database
      DB_CONNECT.connect()

      #check connection success or not
      if DB_CONNECT.get_connection().is_connected():

        #success connection create cursor to execute query
        cursor = DB_CONNECT.get_cursor()
        cursor.execute(sql)
        record = cursor.fetchall()

        #disconnect to database => close cursor and connection
        DB_CONNECT.disconnect()

        return record

    except Exception as e:

      print ("Error in selecting", str(e))

  def update(sql):
    print ("update")

    try:
      
      #connect to database
      DB_CONNECT.connect()

      #check connection success or not
      if DB_CONNECT.get_connection().is_connected():

        #success connection create cursor to execute query
        cursor = DB_CONNECT.get_cursor()
        cursor.execute(sql)
        
        DB_CONNECT.get_connection().commit()

        #disconnect to database => close cursor and connection
        DB_CONNECT.disconnect()

        return cursor.rowcount, "record(s) affected"

    except Exception as e:

      print ("Error in updating", str(e))
  
  def save(sql):
    print ("save")

    try:
      
      #connect to database
      DB_CONNECT.connect()

      #check connection success or not
      if DB_CONNECT.get_connection().is_connected():

        #success connection create cursor to execute query
        cursor = DB_CONNECT.get_cursor()
        cursor.execute(sql)
        
        DB_CONNECT.get_connection().commit()

        #disconnect to database => close cursor and connection
        DB_CONNECT.disconnect()

        return cursor.rowcount, "record(s) affected"

    except Exception as e:

      print ("Error in saving", str(e))

  def select(sql):
    # print ("select")

    try:

      #connect to database
      DB_CONNECT.connect()

      #check connection success or not
      if DB_CONNECT.get_connection().is_connected():

        #success connection create cursor to execute query
        cursor = DB_CONNECT.get_cursor()
        cursor.execute(sql)
        record = cursor.fetchone()

        #disconnect to database => close cursor and connection
        DB_CONNECT.disconnect()

        return record

    except Exception as e:

      print ("Error in selecting", str(e))