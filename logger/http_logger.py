import datetime
import urllib, urllib2

class MyLogger:

    @staticmethod
    def log(log_level, message):
        date_and_message = datetime.datetime.utcnow().isoformat() + "::" + message + "\n"

        if log_level == 3:
            log = "PLSCHECKFFS::" + date_and_message
        elif log_level == 2:
            log = "WARNING::" + date_and_message
        elif log_level == 1:
            log = "INFO::"+ date_and_message

        url = "http://abv.bg"
        log = {"log" : log}

        data = urllib.urlencode(log)
        req = urllib2.Request(url, data)
        rsp = urllib2.urlopen(req)


MyLogger.log(1, "info")
MyLogger.log(2, "warning")
MyLogger.log(3, "fail")
