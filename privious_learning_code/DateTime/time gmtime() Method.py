
# Description
#
# The method gmtime() converts a time expressed in seconds since the epoch to a struct_time in UTC in which the dst flag is always zero. If secs is not provided or None, the current time as returned by time() is used.
# Syntax
#
# Following is the syntax for gmtime() method −
#
# time.gmtime([ sec ])
#
# Parameters
#
#     sec − These are the number of seconds to be converted into structure struct_time representation.
#
# Return Value
#
# This method does not return any value.
# Example
import time

print("time.gmtime() : %s" % time.gmtime())