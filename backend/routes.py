from __main__ import app
from crypt import methods

from Controller.LoginController import LoginController
from Controller.AuthController import AuthController

from Controller.User.UserController import UserController
from Controller.Role.RoleController import RoleController
from Controller.Sensor.SensorController import SensorController
from Controller.SensorCollection.SensorCollectionController import SensorCollectionController
from Controller.SensorManage.SensorManageController import SensorManageController

from Controller.Password.PasswordController import PasswordController

from MasterData.UsersData import UsersData
from Services.ErrorHandlerController import ErrorHandlerController

"""
    Every Error from Python Flask will go to this method
"""
@app.errorhandler(Exception)
def error_handler(e):
    return ErrorHandlerController.errorHandle(e)

""" will validate all APIs except from white lists"""
@app.before_request
def require_authorization():
    return AuthController.require_authorization()

# Creating Master Data
@app.route('/create/master/data/users')
def create_master_data_user():
    return UsersData.create_users()

@app.route('/login/auth', methods=['POST'])
def login_auth():
    return LoginController.login_auth()

@app.route('/logout')
def logout():
    return LoginController.logout()

# password 

@app.route('/forgot_password')
def forgot_password():
    return PasswordController.forgot_password()

@app.route('/send_forgot_password_token', methods=['GET', 'POST'])
def send_forgot_password_token():
    return PasswordController.send_forgot_password_token()

@app.route('/reset_password')
def reset_password():
    return PasswordController.reset_password()

@app.route('/reset_password_and_change', methods=['GET', 'POST'])
def reset_password_and_change():
    return PasswordController.reset_password_and_change()

# sensor
@app.route('/get/sensor/count', methods = ['POST'])
def get_sensor_count():
    return SensorController.get_sensor_count()

@app.route('/get/sensor/list', methods = ['POST'])
def get_sensor_list():
    return SensorController.get_sensor_list()

@app.route('/update/sensor/allow', methods = ['POST'])
def update_sensor_alllow():
    return SensorController.update_sensor_allow()
    
# sensor collection
@app.route('/get/sensor/collection/count', methods = ['POST'])
def get_sensor_collection_count():
    return SensorCollectionController.get_sensor_collection_count()

@app.route('/get/sensor/collection', methods = ['POST'])
def get_sensor_collection():
    return SensorCollectionController.get_sensor_collection()


# sensor manage
@app.route('/get/sensor/manage/status', methods = ['POST'])
def get_sensor_manage_status():
    return SensorManageController.get_sensor_manage_status()

@app.route('/update/sensor/manage/status', methods = ['POST'])
def update_sensor_manage_status():
    return SensorManageController.update_sensor_manage_status()

# user
@app.route('/get/user/count', methods= ['POST'])
def get_user_count():
    return UserController.get_user_count()

@app.route('/get/user', methods= ['POST'])
def get_user():
    return UserController.get_user()

@app.route('/add/user', methods = ['POST'])
def add_user():
    return UserController.add_user()

@app.route('/update/user', methods = ['POST'])
def update_user():
    return UserController.update_user()

@app.route('/user/reset/password', methods = ['POST'])
def user_reset_password():
    return UserController.user_reset_password()

@app.route('/remove/user', methods = ['POST'])
def remove_user():
    return UserController.remove_user()

# role

@app.route('/get/user/role/count', methods = ['POST'])
def get_user_role_count():
    return RoleController.get_role_count()

@app.route('/get/user/role', methods = ['POST'])
def get_user_role():
    return RoleController.get_role()

@app.route('/get/user/roles', methods = ['POST'])
def get_user_roles():
    return RoleController.get_roles()

@app.route('/get/user/role/by/id', methods = ['POST'])
def get_user_role_by_id():
    return RoleController.get_role_by_id()

@app.route('/add/user/role', methods = ['POST'])
def add_user_role():
    return RoleController.add_role()

@app.route('/update/user/role', methods = ['POST'])
def update_user_role():
    return RoleController.update_role()

@app.route('/remove/user/role', methods = ['POST'])
def remove_user_role():
    return RoleController.remove_role()
