#!/usr/bin/env python3

# App name: SMSBOX
# Author: TrollSkull
# Github: https://github.com/TrollSkull
# Version: 1.0

# This script uses the Textbelt API to work
# Textbelt is an API that allows us to send
# a single message per day on a single IP.

try:
    from lib.main import Main, main
    from lib.core.exceptions import MyExceptions
except Exception as err:
    import sys

    print(err, file=sys.stderr)
    sys.exit(1)

if __name__ == "__main__":
    main()