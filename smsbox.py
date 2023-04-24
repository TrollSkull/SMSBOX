#!/usr/bin/env python3

__name__ = 'SMSBOX'
__author__ = 'TrollSkull'
__github__ = 'https://github.com/TrollSkull'
__version__ = '1.1'

# This script uses the Textbelt API to work
# Textbelt is an API that allows us to send
# a single message per day on a single IP.

try:
    import requests
    
except Exception as error:
    import time, os

    print(error + '\nSome requirements are not installed.')
    requirements = ['requests']

    for requirement in requirements:

        print(f'Installing "{requirement}"...')
        os.system(f'pip3 install {requirement}')

        time.sleep(1)

    print('\nRequirements have been installed.')

try:
    from lib.main import Main, main
    from lib.core.exceptions import MyExceptions
except Exception as err:
    import sys

    print(err, file=sys.stderr)
    sys.exit(1)

if __name__ == "__main__":
    main()