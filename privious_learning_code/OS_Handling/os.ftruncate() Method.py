# Description
#
# The method ftruncate() truncates the file corresponding to file descriptor fd, so that it is at most length bytes in size.
# Syntax
#
# Following is the syntax for ftruncate() method −
#
# os.ftruncate(fd, length)
#
# Parameters
#
# fd − This is the file descriptor, which needs to be truncated.
#
# length − This is the length of the file where file needs to be truncated.
#
# Return Value
#
# This method does not return any value.
# Example
import os, sys

# Open a file
fd = os.open("foo.txt", os.O_RDWR | os.O_CREAT)

# Write one string
os.write(fd, "This is test - This is test")

# Now you can use ftruncate() method.
os.ftruncate(fd, 10)

# Now read this file from the beginning.
os.lseek(fd, 0, 0)
str = os.read(fd, 100)
print("Read String is : ", str)

# Close opened file
os.close(fd)

print("Closed the file successfully!!")
