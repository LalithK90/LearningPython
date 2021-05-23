
# Description
#
# The method asctime() converts a tuple or struct_time representing a time as returned by gmtime() or localtime() to
# a 24-character string of the following form: 'Tue Feb 17 23:21:05 2009'. Syntax
#
# Following is the syntax for asctime() method −
#
# time.asctime([t]))
#
# Parameters
#
# t − This is a tuple of 9 elements or struct_time representing a time as returned by gmtime() or localtime() function.
#
# Return Value
#
# This method returns 24-character string of the following form: 'Tue Feb 17 23:21:05 2009'.
# Example

import time

t = time.localtime()
print("time.asctime(t): %s " % time.asctime(t))