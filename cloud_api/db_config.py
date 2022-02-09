"""
    Nay Oo Kyaw
    nayookyaw.nok@gmail.com
"""

from __main__ import app, db

class DB_Config:

  db_username = 'sensor_user'
  db_password = 'P@ssw0rd'
  db_name = 'cloud_sensor_db'

  # db config
  app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://'+ db_username +':' + db_password + '@mysql-db/' + db_name + '?auth_plugin=mysql_native_password'
  app.config['SQLALCHEMY_ECHO'] = False
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  db.init_app(app)

  # import database models
  import Models.Sensor
  import Models.SensorCollection
  import Models.SensorManage

  # run database for tables
  with app.app_context():
    db.create_all()