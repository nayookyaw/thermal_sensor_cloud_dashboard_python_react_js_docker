"""
    Nay Oo Kyaw
    nayookyaw.nok@gmail.com
"""

from flask import render_template, request, jsonify, session, json, abort
from __main__ import app

from Services.Logging.LoggingInfo import LoggingInfo

from Common.TextConstants import TextConstants

from DAO.User.UserRepository import UserRepository
from DAO.Role.RoleRepository import RoleRepository

from datetime import timedelta
import time

from constants import Constants

class AuthController:

    def require_authorization():
        # print(request.endpoint)

        """ 
            check the whitelist routes
            put the route in white list to skip validation with auth
        """
        white_lists_route_array = ['login_auth', 'create_master_data_user', 'forgot_password', 
                                    'send_forgot_password_token', 'reset_password', 'reset_password_and_change']

        # white_lists_route_array = ['*'] # skip all validation
        if '*' in white_lists_route_array:
            return

        if request.endpoint in white_lists_route_array:
            return
            # do nothing
        else : 
            try:

                return
                
                data = request.get_json('data')
                print (data)

                refresh_token = "asdfasdf65/asfd7234sadsdfasdf"

                if refresh_token :
                    c_user = ""
                    if c_user :
                        user = UserRepository.getUserByNameAndToken(c_user, refresh_token)
                        
                        if user:
                            return
                        else:
                            return jsonify({ "status" : "Unauthorized" }), 401
                    else:
                        return jsonify({ "status" : "Unauthorized" }), 401
                else:
                    return jsonify({ "status" : "Unauthorized" }), 401
            
            except Exception as err:
                err_auth = "Error occurs while authenticating " + str(err)
                print (err_auth)
                LoggingInfo.saveErrorLogForDeveloper(err_auth)

                return jsonify({ "status" : err_auth }), 401

            


    