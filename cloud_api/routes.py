"""
    Nay Oo Kyaw
    nayookyaw.nok@gmail.com
"""

from __main__ import app

from Controller.AuthController import AuthController
from Controller.SensorDataController import SensorDataController

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

# sensor data
@app.route('/save/sensor/data', methods = ['POST'])
def save_sensor():
    return SensorDataController.save_sensor()

