import datetime

class MyLogger:

    @staticmethod
    def log(log_level, message):

        date_and_message = datetime.datetime.utcnow().isoformat() + "::" + message + "\033[0m"

        if log_level == 3:
            return "\033[91mPLSCHECKFFS::" + date_and_message
        elif log_level == 2:
            return "\033[93mWARNING::" + date_and_message
        elif log_level == 1:
            return "\033[94mINFO::"+ date_and_message



print MyLogger.log(1, "info")
print MyLogger.log(2, "warning")
print MyLogger.log(3, "fail")
