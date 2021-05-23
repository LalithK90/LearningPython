# Description
#
# The method tcsetpgrp() sets the process group associated with the terminal given by fd (an open file descriptor as returned by os.open()) to pg.
# Syntax
#
# Following is the syntax for tcsetpgrp() method −
#
# os.tcsetpgrp(fd, pg)
#
# Parameters
#
#     fd − This is the file descriptor.
#
#     pg − This set the process group to pg.
#
# Return Value
#
# This method does not return any value.
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

# Setting the process group
os.tcsetpgrp(fd, 2672)
print("done")

os.close(fd)
print("Closed the file successfully!!")
