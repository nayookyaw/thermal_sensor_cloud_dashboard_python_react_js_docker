from flask import render_template, request, jsonify

from Services.Logging.LoggingInfo import LoggingInfo
from Common.TextConstants import TextConstants

from Models.Role import Role
from DAO.Role.RoleRepository import RoleRepository
from DAO.User.UserRepository import UserRepository

from datetime import datetime

class RoleController:

    def get_role_count () :
        try:
            role_count = RoleRepository.getRoleCount()
            LoggingInfo.saveLogging(TextConstants.START_GETTING_ROLE_COUNT)
            if role_count > 0 :
                LoggingInfo.saveLogging(TextConstants.ROLE_COUNT_GET_SUCCESS)
                return jsonify({ "success" : TextConstants.ROLE_COUNT_GET_SUCCESS, "total_count" : role_count }), 200
            else:
                LoggingInfo.saveLogging(TextConstants.NO_DATA)
                return jsonify({ "error" : TextConstants.NO_DATA }), 400
        except Exception as e:
            print (str(e))
            LoggingInfo.saveErrorLogging(TextConstants.ERR_GET_ROLE_COUNT)
            LoggingInfo.saveErrorLogForDeveloper(str(e))
            return jsonify({ "error" : TextConstants.ERR_GET_ROLE_COUNT }), 400

    def get_role () :
        try:
            data = request.get_json('data')
            LoggingInfo.saveLogging(TextConstants.START_GETTING_ROLE)
            if (data):
                roles = RoleRepository.getRole(data)
                res_list = []
                if len(roles) > 0 :
                    for role in roles:
                        res_list.append(role.to_json())
                LoggingInfo.saveLogging(TextConstants.ROLE_GET_SUCCESS)            
                return jsonify({ "success" : TextConstants.ROLE_GET_SUCCESS, "data" : res_list }), 200
            else:
                LoggingInfo.saveLogging(TextConstants.EMPTY_DATA)
                return jsonify({ "error" : TextConstants.EMPTY_DATA }), 400
        except Exception as e:
            print (str(e))
            LoggingInfo.saveErrorLogging(TextConstants.ERR_GET_ROLE)
            LoggingInfo.saveErrorLogForDeveloper(str(e))
            return jsonify({ "error" : TextConstants.ERR_GET_ROLE }), 400

    def get_roles () :
        try:
            LoggingInfo.saveLogging(TextConstants.START_GETTING_ROLE)
            roles = RoleRepository.getRoles()
            res_list = []
            if len(roles) > 0 :
                for role in roles:
                    res_list.append(role.to_json())
            LoggingInfo.saveLogging(TextConstants.ROLE_GET_SUCCESS)            
            return jsonify({ "success" : TextConstants.ROLE_GET_SUCCESS, "data" : res_list }), 200
        except Exception as e:
            print (str(e))
            LoggingInfo.saveErrorLogging(TextConstants.ERR_GET_ROLE)
            LoggingInfo.saveErrorLogForDeveloper(str(e))
            return jsonify({ "error" : TextConstants.ERR_GET_ROLE }), 400

    def get_role_by_id () :
        try:
            data = request.get_json('data')
            # LoggingInfo.saveLogging(TextConstants.START_GETTING_ROLE)
            if (data):
                role = RoleRepository.getRoleById(data['role_id'])
                res_list = []
                if role :
                    res_list.append(role.to_json())
                LoggingInfo.saveLogging(TextConstants.ROLE_GET_SUCCESS)            
                return jsonify({ "success" : TextConstants.ROLE_GET_SUCCESS, "data" : res_list }), 200
            else:
                LoggingInfo.saveLogging(TextConstants.EMPTY_DATA)
                return jsonify({ "error" : TextConstants.EMPTY_DATA }), 400
        except Exception as e:
            print (str(e))
            LoggingInfo.saveErrorLogging(TextConstants.ERR_GET_ROLE)
            LoggingInfo.saveErrorLogForDeveloper(str(e))
            return jsonify({ "error" : TextConstants.ERR_GET_ROLE }), 400

    def add_role():
        data = request.get_json('data')
        LoggingInfo.saveLogging(TextConstants.START_ADDING_ROLE)
        if data:
            role = RoleRepository.getRoleByName(data['role_name'])
            if role == None :
                new_role = Role(
                    role_name = data['role_name'],
                    role = 0,
                    user_creation = 0,
                    user_list = 0,
                )
                if len(data['role_detail']) > 0 :
                    for i in data['role_detail'] :
                        new_role.__setattr__(i, 1)
                RoleRepository.save(new_role)
                LoggingInfo.saveLogging(TextConstants.ROLE_ADD_SUCCESS)
                return jsonify({ "success" : TextConstants.ROLE_ADD_SUCCESS }), 200
            else :
                LoggingInfo.saveLogging(TextConstants.ERR_ROLE)
                return jsonify({ "error" : TextConstants.ERR_ROLE }), 200
        else:
            LoggingInfo.saveLogging(TextConstants.EMPTY_DATA)
            return jsonify({ "error" : TextConstants.EMPTY_DATA }), 400
            
    def update_role():
        data = request.get_json('data')
        LoggingInfo.saveLogging(TextConstants.START_UPDATING_ROLE)
        if data:
            other_role = RoleRepository.getRoleByExceptIdAndName(data['role_id'], data['role_name'])
            if other_role == None :
                updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                role = RoleRepository.getRoleById(data['role_id'])
                if role :
                    role.role_name = data['role_name']
                    role.role = 0
                    role.user_creation = 0
                    role.user_list = 0
                    if len(data['role_detail']) > 0 :
                        for i in data['role_detail'] :
                            role.__setattr__(i, 1)
                    role.updated_at = updated_at
                    RoleRepository.update()

                    LoggingInfo.saveLogging(TextConstants.ROLE_UPDATE_SUCCESS)
                    return jsonify({ "success" : TextConstants.ROLE_UPDATE_SUCCESS }), 200
                else :
                    LoggingInfo.saveLogging(TextConstants.NO_DATA)
                    return jsonify({ "error" : TextConstants.NO_DATA }), 400
            else :
                LoggingInfo.saveLogging(TextConstants.ERR_ROLE)
                return jsonify({ "error" : TextConstants.ERR_ROLE }), 200
        else:
            LoggingInfo.saveLogging(TextConstants.EMPTY_DATA)
            return jsonify({ "error" : TextConstants.EMPTY_DATA }), 400

    def remove_role():
        try:
            data = request.get_json('data')
            LoggingInfo.saveLogging(TextConstants.START_REMOVING_ROLE)
            if data:
                deleted_at =  datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                if data['role_id']:
                    role = RoleRepository.getRoleById(data['role_id'])
                    if role:
                        user = UserRepository.getUserByRoleId(data['role_id'])
                        if user :
                            current_using_role = "This role id, " + str(data['role_id']) + " can't be deleted, current using in user assigned!"
                            LoggingInfo.saveLogging(current_using_role)
                            return jsonify({ "error" : current_using_role }), 400
                        else :
                            role.deleted_at = deleted_at
                            RoleRepository.update()
                            LoggingInfo.saveLogging(TextConstants.ROLE_REMOVE_SUCCESS)
                            return jsonify({ "success" : TextConstants.ROLE_REMOVE_SUCCESS }), 200
                    else:
                        LoggingInfo.saveLogging(TextConstants.NO_ROLE)
                        return jsonify({ "error" : TextConstants.NO_ROLE }), 400
                else:
                    LoggingInfo.saveLogging(TextConstants.EMPTY_DATA)
                    return jsonify({ "error" : TextConstants.EMPTY_DATA }), 400
            else:
                LoggingInfo.saveLogging(TextConstants.EMPTY_DATA)
                return jsonify({ "error" : TextConstants.EMPTY_DATA }),
        except Exception as e:
            print (str(e))
            LoggingInfo.saveErrorLogging(TextConstants.ERR_REMOVE_ROLE)
            LoggingInfo.saveErrorLogForDeveloper(str(e))
            return jsonify({ "error" : TextConstants.ERR_REMOVE_ROLE }), 400
