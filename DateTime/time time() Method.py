# Description
#
# The method time() returns the time as a floating point number expressed in seconds since the epoch, in UTC.
#
# Note − Even though the time is always returned as a floating point number, not all systems provide time with a better precision than 1 second. While this function normally returns non-decreasing values, it can return a lower value than a previous call if the system clock has been set back between the two calls.
# Syntax
#
# Following is the syntax for time() method −
#
# time.time()
#
# Parameters
#
#     NA
#
# Return Value
#
# This method returns the time as a floating point number expressed in seconds since the epoch, in UTC.
# Example
import time

print("time.time(): %f " % time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
