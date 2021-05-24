
# Description
#
# The method altzone() is the attribute of the time module. This returns the offset of the local DST timezone,
# in seconds west of UTC, if one is defined. This is negative if the local DST timezone is east of UTC (as in Western
# Europe, including the UK). Only use this if daylight is nonzero. Syntax
#
# Following is the syntax for altzone() method −
#
# time.altzone
#
# Parameters
#
# NA
#
# Return Value
#
# This method returns the offset of the local DST timezone, in seconds west of UTC, if one is defined.
# Example
import time

print("time.altzone %d " % time.altzone)