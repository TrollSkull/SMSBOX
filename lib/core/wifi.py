from socket import gethostbyname, create_connection, error
from lib.core.utils import Colors
import sys

def CheckWifi():
    try:
        gethostbyname("google.com")
        conexion = create_connection(("google.com", 80), 1)
        conexion.close()

    except error:
        print(Colors.FAIL + "\n[SMSBOX] " + Colors.RESET + "Check your internet connection.")
        sys.exit(1)