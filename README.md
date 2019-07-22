# Date command: A command-based date computation engine

datec allows you to use "date commands" to modify datetime's by adding
to them, like datetime.datetime.now() + Period(2, 'week').

A date command can be parsed from string using the parse() function,
which create a command from a string representation.  This forms the
basis of the datec command, which is a command-line program to output
datetime after applying date commands.  In general the date
representation is NxYYYY-mm-ddTHH:MM:SS.ffffff, where unspecified
parts are omitted leaving the symbols intact, like "2x-2-29T3::." (see
the following for the meaning).  If fractional part is not specified
the "." may be omitted, if all time parts are not specified the "T::."
can be omitted, if all date parts are not specified the "--T" can be
omitted, and if N is 0 the x may be omitted.  By there are a couple
other more formats like +3week and -2wed for shifting by period and
weekday.

Date commands are in two forms: period shifting commands and partial
datetime shifting commands.  The first type is more familiar: they
look like

  * +2week (shift the datetime forward by 2 week)
  * -1month (shift the datetime backward by 1 month)

Period is one of year, month, week, day, hour, minute and second,
represented by an object of the Period class.  Fractional numbers are
acceptable except for year and month.  If shifting a period leads to
an invalid date (e.g., shift backward 1 month from 2019-07-31), it
moves backwards the closest valid date (here, 2019-06-30).  In general
the parts finer than the shifted part is unaffected (e.g., shifting 1
month from 2019-07-31 02:00 gives you 2019-06-30 02:00).

Partial datetime shifting is less familiar.  It looks like:

  * 12:: (set the hour number to 12)
  * +2x12:: (move forward to the second hour 12)
  * +4x--31 (move forward to the fourth occurrence of day 31 of a month)
  * -3x-02-29 (move backward to the third occurrence of February 29)
  * wed (set to the Wednesday of the same week, week starts on Sunday)
  * -3wed (move to the third Wednesday before the current datetime)

They are represented by either a Weekday object or a PartialDate
object with a count.  A count of 0 means setting instead of shifting.
Only integer counts are acceptable.

It is an error to set to an invalid date (e.g., --31 applied on
2019-06-25 is an error).  The datetime parts which are specified must
be consecutive (it is an error to specify 12::05).  It is also an
error to shift for occurrence of partial date with year specified
(e.g., "+2x2019--").

On the other hand, shifting to an invalid date with day number
specified will shift more until a specified date is valid.  For
example, if you add -2-29 with count 1 to 2019-01-01, you end up with
2020-02-29, because 2019-02-29 is not a valid date.  If the count is 2
you get 2024-02-29 instead.

Shifting to invalid date by month will cause the date to moved
backwards until the date is valid.  E.g., if you shift by -6- with
count 1 (next June) from 2019-05-31, you get 2019-06-30.  With count 2
you get 2020-06-30.

This library is grown out of frustration that it is tedious to have a
shell script or program to get a datetime like "the next 6pm from now"
or "the next 3rd of any month from two days ago".  With this module
they can be specified like "+1x18:00:00.0" and "-2day +1x--3"
respectively.  In the expected use cases, counts are small numbers.
So the library is not always efficient (at times we just loop "count"
times to step forward or backward).  Whenever it is simple to do so,
the implementation just forward to relativedelta, in which case they
are more efficient.

At present the program does not handle timezone and daylight saving.
This is bacause the author lives at a place where no daylight saving
is observed.  Contributions are welcome.
