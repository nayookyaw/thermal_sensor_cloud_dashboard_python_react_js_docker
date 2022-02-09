"""
    Nay Oo Kyaw
    nayookyaw.nok@gmail.com
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

import constants

Constants = constants.Constants

app = Flask(__name__, static_url_path=None)

# logging setup
from Services.Logging.LoggingSetup import LoggingSetup
LoggingSetup.startup()

# ----------------------------------------- #
# database configuration start
# declare db connection
db = SQLAlchemy(app)

# migrate database    $ python server.py db migrate    $ python server.py db upgrade
migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db', MigrateCommand, compare_type=True)

# database models
from db_config import DB_Config

# database configuration stop
# ------------------------------------------ #


import routes

if __name__ == '__main__':
    # if you want to migrate database, uncomment the below text
    # manager.run()

    app.run(host= '0.0.0.0', port=5000, debug=True)