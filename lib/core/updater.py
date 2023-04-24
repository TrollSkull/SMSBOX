import requests, urllib.request, sys
from lib.core.utils import Colors
from lib.core.wifi import CheckWifi
from lib.core.utils import Utils

URL = "https://raw.githubusercontent.com/TrollSkull/SMSBOX/master/"

def Update():
    FILES = ['smsbox.py', 'lib/core/wifi.py', 'lib/core/updater.py', 'lib/core/version',
             'lib/core/utils.py', 'lib/main.py', 'lib/core/exceptions.py', 'requirements.txt']
    
    for FL in FILES:
        DATA = urllib.request.urlopen(URL + FL).read()
        
        with open(FL, "wb") as F:
            F.write(DATA)
    
    print(Colors.OK + "\n[SMSBOX]" + Colors.RESET + " Updated successfull, exiting script.")
    sys.exit(0)

def CheckVersion():
    try:
        tool_version = open("./lib/core/version", "r").read()
    except:
        tool_version = "1.0"
    
    try:
        CheckWifi()
        git_version = requests.get("https://raw.githubusercontent.com/TrollSkull/SMSBOX/main/lib/core/version").text  
    except Exception as err:
        import sys

        print(err, file=sys.stderr)
        sys.exit(1)
    
    print(Colors.WORKING + "\n[SMSBOX]" + Colors.RESET +" Verifying Git version...")

    if (tool_version == git_version):
        print(Colors.WARNING + "\n[SMSBOX]" + Colors.RESET + " Version match with GitHub repository.")
        
    else:
        print(Colors.WORKING + "\n[SMSBOX]" + Colors.RESET + " Update available, downloading " + Colors.WORKING + "(" + Colors.OK + Utils.GIT_VERSION + Colors.WORKING + ")...")
        Update()