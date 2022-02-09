"""
    Developed by Nay Oo Kyaw
    nayookyaw.nok@gmail.com
"""

from Services.Logging.LoggingSetup import LoggingSetup

class LoggingInfo:

    def openFilesErrorExcep () :
        # os error 24, too many open files error exception
        # loggerInstList = [LoggingSetup.info_logger, LoggingSetup.error_logger, LoggingSetup.all_logger]
        loggerInstList = [LoggingSetup.info_logger, LoggingSetup.error_logger]
        for loggerInst in loggerInstList :
            for handler in loggerInst.handlers[:]:
                handler.close()
                loggerInst.removeHandler(handler)

    def saveLogging(text):
        info_log = LoggingSetup.get_info_logger()
        # all_log = LoggingSetup.get_all_logger()
        
        #  put text inside info log file
        info_log.info(text)
        LoggingInfo.openFilesErrorExcep()

        # LoggingInfo.openFilesErrorExcep(info_log)
        # save to database
    
    def saveWarningLogging(text):
        info_log = LoggingSetup.get_info_logger()
        # all_log = LoggingSetup.get_all_logger()
        
        info_log.warn(text)
        LoggingInfo.openFilesErrorExcep()
        # LoggingInfo.openFilesErrorExcep(info_log)
    
    def saveErrorLogging(text):
        info_log = LoggingSetup.get_info_logger()
        # all_log = LoggingSetup.get_all_logger()
        if (text):
            info_log.error(text)
            # all_log.error(text)
            LoggingInfo.openFilesErrorExcep()
    
    """ 
        Use this method to see coding error logging
        This method saves the error logging in error.log file
    """
    def saveErrorLogForDeveloper(text):
        error_log = LoggingSetup.get_error_logger()
        # all_log = LoggingSetup.get_all_logger()
        if (text):
            #  put text inside error log file
            error_log.error(text) 
            # all_log.error(text) 
            LoggingInfo.openFilesErrorExcep()