# Description
#
# The method closerange() closes all file descriptors from fd_low (inclusive) to fd_high (exclusive), ignoring errors.This method is introduced in Python version 2.6.
# Syntax
#
# Following is the syntax for closerange() method −
#
# os.closerange(fd_low, fd_high);
#
# Parameters
#
#     fd_low − This is the Lowest file descriptor to be closed.
#
#     fd_high − This is the Highest file descriptor to be closed.
#
# This function is equivalent to −
#
# for fd in xrange(fd_low, fd_high):
#    try:
#       os.close(fd)
#    except OSError:
#       pass
#
# Return Value
#
# This method does not return any value.
# Example
import os, sys

# Open a file
fd = os.open("foo.txt", os.O_RDWR | os.O_CREAT)

# Write one string
os.write(fd, "This is test")

# Close a single opened file
os.closerange(fd, fd)

print("Closed all the files successfully!!")
