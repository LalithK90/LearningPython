print("                     Python - Date & Time\n")

import time;  # This is required to include time module.
import calendar;

ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970:", ticks, "\n")

print("\nGetting current time\n")
localtime = time.localtime(time.time())
print("Local current time :", localtime)
print("\nGetting formatted time\n")
localtime1 = time.asctime(time.localtime(time.time()))
print("Local current time :", localtime1)
print("\nGetting calendar for a month\n")
cal = calendar.month(2008, 1)
print("Here is the calendar:")
print(cal)

print("                                 Time module\n")

print(
    "\nThe offset of the local DST timezone, in seconds west of UTC, if one is defined. This is negative if the local DST timezone is east of UTC (as in Western Europe, including the UK). Only use this if daylight is nonzero.\n")
print("\nAccepts a time-tuple and returns a readable 24-character string such as 'Tue Dec 11 18:07:14 2008'.\n")
print(
    "\nReturns the current CPU time as a floating-point number of seconds. To measure computational costs of different approaches, the value of time.clock is more useful than that of time.time().\n")
print("\nLike asctime(localtime(secs)) and without arguments is like asctime( )\n")
print(
    "\nAccepts an instant expressed in seconds since the epoch and returns a time-tuple t with the UTC time. Note : t.tm_isdst is always 0\n")
print(
    "\nAccepts an instant expressed in seconds since the epoch and returns a time-tuple t with the local time (t.tm_isdst is 0 or 1, depending on whether DST applies to instant secs by local rules).\n")
print(
    "\nAccepts an instant expressed as a time-tuple in local time and returns a floating-point value with the instant expressed in seconds since the epoch.\n")
print("\nSuspends the calling thread for secs seconds.\n")
print(
    "\nAccepts an instant expressed as a time-tuple in local time and returns a string representing the instant as specified by string fmt.\n")
print("\nParses str according to format string fmt and returns the instant in time-tuple format.\n")
print("\nReturns the current time instant, a floating-point number of seconds since the epoch.\n")
print(
    "\nResets the time conversion rules used by the library routines. The environment variable TZ specifies how this is done.\n")

print("\nThe datetime Module\n")
print("\nThe pytz Module\n")
print("\nThe dateutil Module\n")
