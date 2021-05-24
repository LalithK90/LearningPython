# Description
#
# The method popen() opens a pipe to or from command.The return value is an open file object connected to the pipe, which can be read or written depending on whether mode is 'r' (default) or 'w'.The bufsize argument has the same meaning as in open() function.
# Syntax
#
# Following is the syntax for popen() method −
#
# os.popen(command[, mode[, bufsize]])
#
# Parameters
#
# command − This is command used.
#
# mode − This is the Mode can be 'r'(default) or 'w'.
#
# bufsize − If the buffering value is set to 0, no buffering will take place. If the buffering value is 1, line buffering will be performed while accessing a file. If you specify the buffering value as an integer greater than 1, then buffering action will be performed with the indicated buffer size. If negative, the buffer size is the system default(default behavior).
#
# Return Value
#
# This method returns an open file object connected to the pipe.
# Example
import os, sys

# using command mkdir
a = 'mkdir nwdir'

b = os.popen(a, 'r', 1)

print(b)
