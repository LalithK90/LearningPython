# Description
#
# The method dup() returns a duplicate of file descriptor fd which can be used in place of original descriptor.
# Syntax
#
# Following is the syntax for dup() method −
#
# os.dup(fd);
#
# Parameters
#
#     fd − This is the original file descriptor.
#
# Return Value
#
# This method returns a duplicate of file descriptor.
# Example
import os, sys

# Open a file
fd = os.open("foo.txt", os.O_RDWR | os.O_CREAT)

# Get one duplicate file descriptor
d_fd = os.dup(fd)

# Write one string using duplicate fd
os.write(d_fd, "This is test")

# Close a single opened file
os.closerange(fd, d_fd)

print("Closed all the files successfully!!")
