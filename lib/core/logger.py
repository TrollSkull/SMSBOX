import logging, os

from lib.core.utils import Utils
from lib.core.wifi import CheckWifi

class Logger:
    def logged(message, number, response):
        log_dir = os.getcwd() + '\logs'

        if os.path.isfile(log_dir + Utils.DATE_FILE + ".log") == True:
            logging.info('\n')
        else:
            logging.basicConfig(filename = (log_dir + Utils.DATE_FILE + ".log"), level=logging.DEBUG, format='')

            template = "SMSBOX Debug Log, taken on " + Utils.DATE + ".\n"
            logging.info(str(template))

        logging.info(f'[INFO - {Utils.TIME}] Message sent to: "' + number + '" at ' + Utils.DATE_LOG)
        logging.info(f'[INFO - {Utils.TIME}] Message: "' + message + '"')
        logging.info(f'[INFO - {Utils.TIME}] Response: {response}\n')