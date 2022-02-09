from __main__ import app, db

class DB_Config:

  db_username = 'sensor_user'
  db_password = 'P@ssw0rd'
  db_name = 'cloud_sensor_db'
  db_host = 'mysql-db'

  # db config
  app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://'+ db_username +':' + db_password + '@' + db_host + '/' + db_name + '?auth_plugin=mysql_native_password'
  app.config['SQLALCHEMY_ECHO'] = False
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  db.init_app(app)

  # import database models
  import Models.User
  import Models.Role

  # run database for tables
  with app.app_context():
    db.create_all()