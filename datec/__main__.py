import sys
import datetime

import datec

if __name__ == '__main__':
    dt = datetime.datetime.now()
    for cmd in sys.argv[1:]:
        dt = dt + datec.parse(cmd.lower())
    print(dt.isoformat())
