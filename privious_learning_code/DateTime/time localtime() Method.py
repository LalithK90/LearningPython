
# Description
#
# The method localtime() is similar to gmtime() but it converts number of seconds to local time. If secs is not provided or None, the current time as returned by time() is used. The dst flag is set to 1 when DST applies to the given time.
# Syntax
#
# Following is the syntax for localtime() method −
#
# time.localtime([ sec ])
#
# Parameters
#
# sec − These are the number of seconds to be converted into structure struct_time representation.
#
# Return Value
#
# This method does not return any value.
# Example
import time

print("time.localtime() : %s" % time.localtime())