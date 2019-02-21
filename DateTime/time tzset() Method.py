
# Description
#
# The method tzset() resets the time conversion rules used by the library routines. The environment variable TZ
# specifies how this is done.
#
# The standard format of the TZ environment variable is (whitespace added for clarity) −
#
# std offset [dst [offset [,start[/time], end[/time]]]]
#
# std and dst − Three or more alphanumerics giving the timezone abbreviations. These will be propagated into
# time.tzname.
#
# offset − The offset has the form − .hh[:mm[:ss]]. This indicates the value added the local time to arrive at UTC.
# If preceded by a '-', the timezone is east of the Prime Meridian; otherwise, it is west. If no offset follows dst,
# summer time is assumed to be one hour ahead of standard time.
#
# start[/time], end[/time] − Indicates when to change to and back from DST. The format of the start and end dates are
# one of the following −
#
# Jn − The Julian day n (1 <= n <= 365). Leap days are not counted, so in all years February 28 is day 59 and March 1
# is day 60.
#
# n − The zero-based Julian day (0 <= n <= 365). Leap days are counted, and it is possible to refer to February 29.
#
# Mm.n.d − The d'th day (0 <= d <= 6) or week n of month m of the year (1 <= n <= 5, 1 <= m <= 12, where week 5 means
# 'the last d day in month m' which may occur in either the fourth or the fifth week). Week 1 is the first week in
# which the d'th day occurs. Day zero is Sunday.
#
# time − This has the same format as offset except that no leading sign ('-' or '+') is allowed. The default,
# if time is not given, is 02:00:00.
#
# Syntax
#
# Following is the syntax for tzset() method −
#
# time.tzset()
#
# Parameters
#
#     NA
#
# Return Value
#
# This method does not return any value.
# Example
import time
import os

os.environ['TZ'] = 'EST+05EDT,M4.1.0,M10.5.0'
time.tzset()
print(time.strftime('%X %x %Z'))

os.environ['TZ'] = 'AEST-10AEDT-11,M10.5.0,M3.5.0'
time.tzset()
print(time.strftime('%X %x %Z'))