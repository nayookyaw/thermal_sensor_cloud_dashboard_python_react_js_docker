"""
    Nay Oo Kyaw
    nayookyaw.nok@gmail.com
"""

from flask import request, jsonify

from Common.TextConstants import TextConstants
from Services.Logging.LoggingInfo import LoggingInfo

from constants import Constants

class AuthController:

    def require_authorization():

        """ 
            check the whitelist routes
            put the route in white list to skip validation with auth
        """
        white_lists_route_array = ['test_route', 'test_route1']

        # white_lists_route_array = ['*'] # skip all validation
        if '*' in white_lists_route_array:
            return

        if request.endpoint in white_lists_route_array:
            return
            # do nothing
        else :       
            try:
                input_req = request.form
                input_dict = input_req.to_dict(flat=False)

                # check the input validation
                if (len(input_dict) <= 0):
                    return jsonify({ "status" : TextConstants.INVALID_INPUT}), 400
                
                mac_address = input_dict['mac_address'][0]
                sensor_data_str = input_dict['sensor_data'][0]
                api_key = input_dict['api_key'][0]

                if (mac_address and sensor_data_str and api_key):
                    if (api_key == Constants.API_KEY):
                        # pass the authentication
                        return
                    else:
                        LoggingInfo.saveLogging(TextConstants.INVLAID_API_KEY)
                        return jsonify({ "status" : TextConstants.INVLAID_API_KEY }), 401
                else:
                    return jsonify({ "status" : TextConstants.INVALID_INPUT}), 400

                
            except Exception as e:
                LoggingInfo.saveErrorLogForDeveloper(TextConstants.ERR_AUTH_CHECK + " " + str(e))
                return jsonify({ "status" : TextConstants.ERR_AUTH_CHECK }), 400
            


    