
# Description
#
# The method sleep() suspends execution for the given number of seconds. The argument may be a floating point number to indicate a more precise sleep time.
#
# The actual suspension time may be less than that requested because any caught signal will terminate the sleep() following execution of that signal's catching routine.
# Syntax
#
# Following is the syntax for sleep() method −
#
# time.sleep(t)
#
# Parameters
#
# t − This is the number of seconds execution to be suspended.
#
# Return Value
#
# This method does not return any value.
# Example
import time

print("Start : %s" % time.ctime())
time.sleep( 5 )
print("End : %s" % time.ctime())