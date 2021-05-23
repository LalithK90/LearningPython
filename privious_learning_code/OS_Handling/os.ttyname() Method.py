
# Description
#
# The method ttyname() returns a string, which specifies the terminal device associated with fd. If fd is not associated with a terminal device, an exception is raised.
# Syntax
#
# Following is the syntax for ttyname() method −
#
# os.ttyname(fd)
#
# Parameters
#
#     fd − This is the file descriptor.
#
# Return Value
#
# This method returns a string which specifies the terminal device.
# Example
import os, sys

# Showing current directory
print("Current working dir :%s" %os.getcwd())

# Changing dir to /dev/tty
fd = os.open("/dev/tty",os.O_RDONLY)

p = os.ttyname(fd)
print("the terminal device associated is: ")
print(p)
print("done!!")

os.close(fd)
print("Closed the file successfully!!")