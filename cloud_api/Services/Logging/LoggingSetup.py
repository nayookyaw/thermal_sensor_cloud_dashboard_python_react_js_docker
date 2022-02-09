"""
    Developed by Nay Oo Kyaw
    nayookyaw.nok@gmail.com
"""

import logging
import os, stat

from constants import Constants
from datetime import date, datetime

fromatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

class LoggingSetup:

    all_logger = ''
    info_logger = ''
    error_logger = ''

    def setup_logger (logger_name, log_file, level=logging.INFO):
        # LOG_PATH = Constants.ALL_LOG_PATH + date.today().strftime("%Y-%m-%d") + '/' + str(datetime.now().minute)
        LOG_PATH = Constants.ALL_LOG_PATH + date.today().strftime("%Y-%m-%d")
        if not os.path.exists(LOG_PATH):
            LoggingSetup.mkdir_p(LOG_PATH)
        filename = LOG_PATH + log_file

        # alllogs_filename = LOG_PATH + "/alllogs.log"
        # logging.basicConfig(filename=alllogs_filename, level=level)
        logging.basicConfig(level=level)

        """ Separate Log file """
        handler = logging.FileHandler(filename)
        handler.setFormatter(fromatter)
        # handler.setLevel(level)
        # logging.root.handlers = [handler]

        logger = logging.getLogger(logger_name)
        logger.setLevel(level)
        # logger.addHandler(handler)

        logger.handlers[:] = [handler]
        
        return logger

    def startup() :
        LoggingSetup.get_info_logger()
        LoggingSetup.get_error_logger()
        # LoggingSetup.get_all_logger()
    
    def get_info_logger():
        info_file = "/info.log"
        LoggingSetup.info_logger = LoggingSetup.setup_logger('info_logger', info_file, logging.INFO)
        return LoggingSetup.info_logger
    
    def get_error_logger():
        error_file = "/error.log"
        LoggingSetup.error_logger = LoggingSetup.setup_logger('error_logger', error_file, logging.ERROR)
        # LoggingSetup.error_logger.error("Error Handling is launched!")
        return LoggingSetup.error_logger

    def get_all_logger():
        all_file = "/alllogs.log"
        LoggingSetup.all_logger = LoggingSetup.setup_logger('all_logger', all_file, logging.DEBUG)
        return LoggingSetup.all_logger

    def mkdir_p(path):
        """http://stackoverflow.com/a/600612/190597 (tzot)"""
        try:
            os.makedirs(path, exist_ok=True)  # Python>3.2
        except TypeError:
            try:
                os.makedirs(path)
            except OSError as exc: # Python >2.5
                if exc.errno == errno.EEXIST and os.path.isdir(path):
                    pass
                else: raise
        finally:
            print ("Log file creation was succeed")
