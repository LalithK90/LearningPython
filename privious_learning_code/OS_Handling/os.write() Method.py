
# Description
#
# The method write() writes the string str to file descriptor fd. Return the number of bytes actually written.
# Syntax
#
# Following is the syntax for write() method −
#
# os.write(fd, str)
#
# Parameters
#
#     fd − This is the file descriptor.
#
#     str − This is the string to be written.
#
# Return Value
#
# This method returns the number of bytes actually written.
# Example
import os, sys

# Open file
fd = os.open("f1.txt",os.O_RDWR|os.CREAT)

# Writing text
ret = os.write(fd,"This is test")

# ret consists of number of bytes written to f1.txt
print("the number of bytes written: ")
print(ret)

print("written successfully")

# Close opened file
os.close(fd)
print("Closed the file successfully!!")