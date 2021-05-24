# Description
#
# The method close() closes the associated with file descriptor fd.
# Syntax
#
# Following is the syntax for close() method −
#
# os.close(fd);
#
# Parameters
#
# fd − This is the file descriptor of the file.
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

# Close opened file
os.close(fd)

print("Closed the file successfully!!")
