from flask import render_template, request, jsonify

from Common.TextConstants import TextConstants

from Models.User import User
from DAO.User.UserRepository import UserRepository

from datetime import datetime

from Services.EncryptDecrypt import EncryptDecrypt
from Services.Logging.LoggingInfo import LoggingInfo

class UserController:

    def get_user_count () :
        try:
            user_count = UserRepository.getUserCount()
            LoggingInfo.saveLogging(TextConstants.START_GETTING_USER_COUNT)
            if user_count > 0 :
                LoggingInfo.saveLogging(TextConstants.USER_COUNT_GET_SUCCESS)
                return jsonify({ "success" : TextConstants.USER_COUNT_GET_SUCCESS, "total_count" : user_count }), 200
            else:
                LoggingInfo.saveLogging(TextConstants.NO_DATA)
                return jsonify({ "error" : TextConstants.NO_DATA }), 400
        except Exception as e:
            print (str(e))
            LoggingInfo.saveErrorLogging(TextConstants.ERR_GET_USER_COUNT)
            LoggingInfo.saveErrorLogForDeveloper(str(e))
            return jsonify({ "error" : TextConstants.ERR_GET_USER_COUNT }), 400

    def get_user () :
        try:
            data = request.get_json('data')
            LoggingInfo.saveLogging(TextConstants.START_GETTING_USER)
            if (data):
                users = UserRepository.getUsers(data)
                res_list = []
                if len(users) > 0 :
                    for user in users:
                        temp = user[0].to_json()
                        temp['role_name'] = user[1]
                        res_list.append(temp)
                LoggingInfo.saveLogging(TextConstants.USER_GET_SUCCESS)            
                return jsonify({ "success" : TextConstants.USER_GET_SUCCESS, "data" : res_list }), 200
            else:
                LoggingInfo.saveLogging(TextConstants.EMPTY_DATA)
                return jsonify({ "error" : TextConstants.EMPTY_DATA }), 400
        except Exception as e:
            print (str(e))
            LoggingInfo.saveErrorLogging(TextConstants.ERR_GET_USER)
            LoggingInfo.saveErrorLogForDeveloper(str(e))
            return jsonify({ "error" : TextConstants.ERR_GET_USER }), 400

    def add_user():
        try:
            data = request.get_json('data')
            LoggingInfo.saveLogging(TextConstants.START_ADDING_USER)
            if data:
                user = UserRepository.searchUserByName(data['username'])
                if user == None :
                    new_user = User(
                        username = data['username'],
                        email = data['email'],
                        password = str(EncryptDecrypt.encrypt(data['password'])),
                        phone = data['phone'],
                        role_id = data['role_id'],
                    )
                    UserRepository.save(new_user)
                    LoggingInfo.saveLogging(TextConstants.USER_ADD_SUCCESS)
                    return jsonify({ "success" : TextConstants.USER_ADD_SUCCESS }), 200
                else :
                    LoggingInfo.saveLogging(TextConstants.ERR_USER)
                    return jsonify({ "error" : TextConstants.ERR_USER }), 200
            else:
                LoggingInfo.saveLogging(TextConstants.EMPTY_DATA)
                return jsonify({ "error" : TextConstants.EMPTY_DATA }), 400
        except Exception as e:
            print (str(e))
            LoggingInfo.saveErrorLogging(TextConstants.ERR_ADD_USER)
            LoggingInfo.saveErrorLogForDeveloper(str(e))
            return jsonify({ "error" : TextConstants.ERR_ADD_USER }), 400

    def update_user():
        try:
            data = request.get_json('data')
            LoggingInfo.saveLogging(TextConstants.START_UPDATING_USER)
            if data:
                other_user = UserRepository.getUserByExceptIdAndName(data['id'], data['username'])
                if other_user == None :
                    # updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    user = UserRepository.getUserById(data['id'])
                    if user :
                        user.username = data['username'],
                        user.email = data['email'],
                        user.phone = data['phone']
                        user.role_id = data['role_id']
                        # user.updated_at = updated_at
                        UserRepository.update()
                        LoggingInfo.saveLogging(TextConstants.USER_UPDATE_SUCCESS)
                        return jsonify({ "success" : TextConstants.USER_UPDATE_SUCCESS }), 200
                    else :
                        LoggingInfo.saveLogging(TextConstants.NO_DATA)
                        return jsonify({ "error" : TextConstants.NO_DATA }), 400 
                else :
                    LoggingInfo.saveLogging(TextConstants.ERR_USER)
                    return jsonify({ "error" : TextConstants.ERR_USER }), 200
            else:
                LoggingInfo.saveLogging(TextConstants.EMPTY_DATA)
                return jsonify({ "error" : TextConstants.EMPTY_DATA }), 400
        except Exception as e:
            print (str(e))
            LoggingInfo.saveErrorLogging(TextConstants.ERR_UPDATE_USER)
            LoggingInfo.saveErrorLogForDeveloper(str(e))
            return jsonify({ "error" : TextConstants.ERR_UPDATE_USER }), 400

    def user_reset_password():
        try:
            data = request.get_json('data')
            LoggingInfo.saveLogging(TextConstants.START_RESETTING_PASSWORD_USER)
            if data:
                user = UserRepository.getUserById(data['id'])
                if user:
                    user.password = str(EncryptDecrypt.encrypt(data['password']))
                    user.token = None
                    UserRepository.update()
                    LoggingInfo.saveLogging(TextConstants.USER_RESET_PASSWORD_SUCCESS)
                    return jsonify({ "success" : TextConstants.USER_RESET_PASSWORD_SUCCESS }), 200
            else:
                LoggingInfo.saveLogging(TextConstants.EMPTY_DATA)
                return jsonify({ "error" : TextConstants.EMPTY_DATA }), 400
        except Exception as e:
            print (str(e))
            LoggingInfo.saveErrorLogging(TextConstants.ERR_ADD_USER)
            LoggingInfo.saveErrorLogForDeveloper(str(e))
            return jsonify({ "error" : TextConstants.ERR_ADD_USER }), 400

    def remove_user():
        try:
            data = request.get_json('data')
            LoggingInfo.saveLogging(TextConstants.START_REMOVING_USER)
            if data:
                deleted_at =  datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                if data['id']:
                    user = UserRepository.getUserById(data['id'])
                    if user:
                        user.deleted_at = deleted_at
                        UserRepository.update()
                        LoggingInfo.saveLogging(TextConstants.USER_REMOVE_SUCCESS)
                        return jsonify({ "success" : TextConstants.USER_REMOVE_SUCCESS }), 200
                    else:
                        LoggingInfo.saveLogging(TextConstants.NO_DATA)
                        return jsonify({ "error" : TextConstants.NO_DATA }), 400
                else:
                    LoggingInfo.saveLogging(TextConstants.EMPTY_DATA)
                    return jsonify({ "error" : TextConstants.EMPTY_DATA }), 400
            else:
                LoggingInfo.saveLogging(TextConstants.EMPTY_DATA)
                return jsonify({ "error" : TextConstants.EMPTY_DATA }),
        except Exception as e:
            print (str(e))
            LoggingInfo.saveErrorLogging(TextConstants.ERR_REMOVE_USER)
            LoggingInfo.saveErrorLogForDeveloper(str(e))
            return jsonify({ "error" : TextConstants.ERR_REMOVE_USER }), 400
