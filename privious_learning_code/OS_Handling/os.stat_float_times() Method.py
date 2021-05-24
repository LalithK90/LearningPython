
# Description
#
# The method stat_float_times() determines whether stat_result represents time stamps as float objects.
# Syntax
#
# Following is the syntax for stat_float_times() method −
#
# os.stat_float_times([newvalue])
#
# Parameters
#
# newvalue − If newvalue is True, future calls to stat() return floats, if it is False, future call on stat returns ints. If newvalue is not mentioned, it returns the current settings.
#
# Return Value
#
# This method returns either True or False.
# Example
import os, sys

# Stat information
statinfo = os.stat('a2.py')

print(statinfo)
statinfo = os.stat_float_times()
print(statinfo)