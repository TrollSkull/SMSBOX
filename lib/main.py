class Main:
  try:
    import requests, time, sys

    from lib.core.utils import (
          Banner, Colors,
          Utils, CheckOSClear
    )

    from lib.core.logger import Logger
    from lib.core.wifi import CheckWifi
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
        phone_number = phone_number.replace(" ", "")

        message = input(Colors.OK + "Enter the message: " + Colors.RESET)

        if "+" not in phone_number:
          print(Colors.FAIL + "\n[SMSBOX]" + Colors.RESET + " Could not send message!\n")
          print(Colors.FAIL + "The country code has not been entered.")
          sys.exit(1)

        send_message = requests.post('https://textbelt.com/text', {
          'phone': phone_number,
          'message': message,
          'key': 'textbelt'})
        
          # If you have a Textbelt KEY you can put it here.
          # You can buy a KEY visiting "https://textbelt.com/purchase/".
        
        response_data = send_message.json()

        if response_data['success'] == False:
          print(Colors.FAIL + "\n[SMSBOX]" + Colors.RESET + " Could not send message!\n")
          Logger.logged(message=message, number=phone_number, response=response_data)

          if response_data['quotaRemaining'] == 0:
                    
            print(Colors.FAIL + response_data['error'])
            print(Colors.WORKING + "Your remaining messages: " + Colors.RESET + str(response_data['quotaRemaining']))
            sys.exit(1)

          else:
            print(response_data['error'])
            sys.exit(1)

        else:
          print(Colors.OK + "\n[SMSBOX]" + Colors.RESET + " The message has been sent successfully at " + Utils.TIME + "!")
          Logger.logged(message=message, number=phone_number, response=response_data)
          
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