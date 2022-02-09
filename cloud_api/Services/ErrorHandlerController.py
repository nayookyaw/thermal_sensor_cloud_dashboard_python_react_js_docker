"""
    Developed by Nay Oo Kyaw
    nayookyaw.nok@gmail.com
"""

from flask import render_template, request, jsonify
from __main__ import app

from Services.Logging.LoggingSetup import LoggingSetup

class ErrorHandlerController:
    def errorHandle(e):

        error_log = LoggingSetup.get_error_logger()
        error_log.error(e)

        # to show all logs
        app.logger.exception(e)

        print (e)

        return jsonify({ "error" : str(e) }), 500