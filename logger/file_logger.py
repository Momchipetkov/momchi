import datetime

class MyLogger:

    @staticmethod
    def log(log_level, message):
        store_messsage = open("./log", "a");

        date_and_message = datetime.datetime.utcnow().isoformat() + "::" + message + "\n"

        if log_level == 3:
            store_messsage.write("PLSCHECKFFS::" + date_and_message)
        elif log_level == 2:
            store_messsage.write("WARNING::" + date_and_message)
        elif log_level == 1:
            store_messsage.write("INFO::"+ date_and_message)


MyLogger.log(1, "info")
MyLogger.log(2, "warning")
MyLogger.log(3, "fail")
