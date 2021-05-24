# Description
#
# The method tcgetpgrp() returns the process group associated with the terminal given by fd (an open file descriptor as returned by os.open())
# Syntax
#
# Following is the syntax for tcgetpgrp() method −
#
# os.tcgetpgrp(fd)
#
# Parameters
#
# fd − This is the file descriptor.
#
# Return Value
#
# This method returns the process group.
# Example
import os, sys

# Showing current directory
print("Current working dir :%s" % os.getcwd())

# Changing dir to /dev/tty
fd = os.open("/dev/tty", os.O_RDONLY)

f = os.tcgetpgrp(fd)

# Showing the process group
print("the process group associated is: ")
print(f)

os.close(fd)
print("Closed the file successfully!!")
