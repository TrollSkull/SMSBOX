import sys, os, requests, datetime

class Colors:
    OK = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    RESET = '\033[0m'
    WORKING = '\033[34m'
    GRAY = '\033[1;30m'

class Utils:
    NOW = datetime.datetime.now()
    DATE = NOW.strftime("[%y-%m-%d]") 
    TIME = NOW.strftime("%H:%M")
    DATE_FILE = NOW.strftime("/%y-%m-%d")
    DATE_LOG = NOW.strftime("%y-%m-%d")

    TOOL_VERSION = open("./lib/core/version", "r").read()
    GIT_VERSION = requests.get("https://raw.githubusercontent.com/TrollSkull/SMSBOX/main/lib/core/version").text  

def CheckOSClear():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

def Banner():
    print(Colors.OK + """
 ___      ___ __  __ ___ ___  _____  __
|_|_|_   / __|  \/  / __| _ )/ _ \ \/ /
|_|_|_|  \__ \ |\/| \__ \ _ \ (_) >  < 
|_|_|_|  |___/_|  |_|___/___/\___/_/\_\\
    """ + Colors.RESET)

    print(Colors.OK + "[" + Colors.RESET + "1" + Colors.OK + "] Message" + Colors.RESET + "         -   " + Colors.WORKING + "Send a message!")
    print(Colors.OK + "[" + Colors.RESET + "2" + Colors.OK + "] Update script" + Colors.RESET + "   -   " + Colors.WORKING + "Version (" + Colors.OK + Utils.TOOL_VERSION + Colors.WORKING + ")")
    print(Colors.OK + "[" + Colors.RESET + "3" + Colors.OK + "] Exit" + Colors.RESET + "            -   " + Colors.WORKING + "Close script!" + Colors.RESET)