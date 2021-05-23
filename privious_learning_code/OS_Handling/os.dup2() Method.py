# Description
#
# The method dup2() duplicates file descriptor fd to fd2, closing the latter first if necessary.
#
# Note − New file description would be assigned only when it is available. In the following example given below, 1000 would be assigned as a duplicate fd in case when 1000 is available.
# Syntax
#
# Following is the syntax for dup2() method −
#
# os.dup2(fd, fd2);
#
# Parameters
#
#     fd − This is File descriptor to be duplicated.
#
#     fd2 − This is Duplicate file descriptor.
#
# Return Value
#
# This method returns a duplicate of file descriptor.
# Example
import os, sys

# Open a file
fd = os.open("foo.txt", os.O_RDWR | os.O_CREAT)

# Write one string
os.write(fd, "This is test")

# Now duplicate this file descriptor as 1000
fd2 = 1000
os.dup2(fd, fd2);

# Now read this file from the beginning using fd2.
os.lseek(fd2, 0, 0)
str = os.read(fd2, 100)
print("Read String is : ", str)

# Close opened file
os.close(fd)

print("Closed the file successfully!!")
