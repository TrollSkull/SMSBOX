class Main:
  try:
    import requests
    import time
    import sys

    from lib.core.utils import Colors
    from lib.core.utils import Banner
    from lib.core.utils import CheckOSClear
    from lib.core.utils import Utils

    from lib.core.wifi import CheckWifi
    from lib.core.updater import Update
    from lib.core.updater import CheckVersion

    CheckOSClear()
    Banner()
    CheckWifi()

  except Exception as err:
    from lib.core.exceptions import MyExceptions
    raise MyExceptions(str(err)) 
  
  try:
    while True:
      option = str(input("\nSMSBOX " + Colors.OK + "~# " + Colors.RESET))

      if option == "1":
        phone_number = input(Colors.OK + "\nEnter the number with country code: " + Colors.RESET)
        message = input(Colors.OK + "Enter the message: " + Colors.RESET)

        send_message = requests.post('https://textbelt.com/text', {
          'phone': phone_number,
          'message': message,
          'key': 'textbelt'})

        response_data = send_message.json()

        if response_data['success'] == False:
          print(Colors.FAIL + "\n[SMSBOX]" + Colors.RESET + " Could not send message!\n")

          if response_data['quotaRemaining'] == 0:
                    
            print(Colors.FAIL + response_data['error'])
            print(Colors.WORKING + "Your remaining messages: " + Colors.RESET + str(response_data['quotaRemaining']))

          else:
            print(response_data['error'])

        else:
          print(Colors.OK + "\n[SMSBOX]" + Colors.RESET + " The message has been sent successfully!")

      elif option == "2":
        CheckVersion()

      elif option == "3":
        print(Colors.OK + "\n[SMSBOX] " + Colors.RESET + "Bye bye!")
        sys.exit(0)

      else:
        print(Colors.FAIL + "\n[SMSBOX] " + Colors.RESET + "Command not found!")
        time.sleep(2)

  except KeyboardInterrupt:
      print (Colors.WARNING + "\n[SMSBOX] " + Colors.RESET + "Keyboard interrupt detected, exiting.")
      sys.exit(1)

def main():
    try:
        smsbox = Main()
        smsbox
    except Exception as err:
        import sys

        print(err, file=sys.stderr)
        sys.exit(1)
