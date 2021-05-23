
# Description
#
# The method read() reads at most n bytes from file desciptor fd, return a string containing the bytes read. If the end of file referred to by fd has been reached, an empty string is returned.
# Syntax
#
# Following is the syntax for read() method −
#
# os.read(fd,n)
#
# Parameters
#
#     fd − This is the file descriptor of the file.
#
#     n − These are n bytes from file descriptor fd.
#
# Return Value
#
# This method returns a string containing the bytes read.
# Example
import os, sys

# Open a file
fd = os.open("f1.txt", os.O_RDWR)

# Reading text
ret = os.read(fd, 12)
print(ret)

# Close opened file
os.close(fd)
print("Closed the file successfully!!")
