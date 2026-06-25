from __future__ import print_function

import datetime
import sys
import time

import datec


def main() -> None:
    dt = datetime.datetime.now()
    wait = False
    for cmd in sys.argv[1:]:
        if cmd == '-h':
            print('''Date command

Usage: datec [-w] [<command>] ...

Datec starts from the current time and apply commands.  Normally the
ending datetime is printed in ISO YYYY-MM-DDTHH:MM:SS.ffffff format.
But if -w is given, no output is printed; instead the program sleeps
until the ending datetime.

<command> may be of the following forms:

  * +2week: shift two weeks ahead
  * mon: set to to the Monday of the current week
  * +2mon: shift two Mondays ahead
  * -3-7T14:: set month to 3, day to 7, and hour to 14
  * +2x--31: move forward by 2 month day 31 (months without a 31st
    day does not count.

''', file=sys.stderr)
            sys.exit(0)
        if cmd == '-w':
            wait = True
            continue
        dt = dt + datec.parse(cmd.lower())
    if wait:
        delta = (dt - datetime.datetime.now()).total_seconds()
        if delta > 0:
            time.sleep(delta)
    else:
        print(dt.isoformat())


if __name__ == '__main__':
    main()
