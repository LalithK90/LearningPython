
# Description
#
# The method isatty()returns True if the file descriptor fd is open and connected to a tty(-like) device, else False.
# Syntax
#
# Following is the syntax for isatty() method −
#
# os.isatty( fd )
#
# Parameters
#
#     fd − This is the file descriptor for which association needs to be checked.
#
# Return Value
#
# This method returns True if the file descriptor fd is open and connected to a tty(-like) device, else False.
# Example
import os, sys

# Open a file
fd = os.open( "foo.txt", os.O_RDWR|os.O_CREAT )

# Write one string
os.write(fd, "This is test")

# Now use isatty() to check the file.
ret = os.isatty(fd)

print("Returned value is: ", ret)

# Close opened file
os.close( fd )