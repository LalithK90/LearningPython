# Description
#
# The method lseek() sets the current position of file descriptor fd to the given position pos, modified by how.
# Syntax
#
# Following is the syntax for lseek() method −
#
# os.lseek(fd, pos, how)
#
# Parameters
#
# fd − This is the file descriptor, which needs to be processed.
#
# pos − This is the position in the file with respect to given parameter how. You give os.SEEK_SET or 0 to set the position relative to the beginning of the file, os.SEEK_CUR or 1 to set it relative to the current position; os.SEEK_END or 2 to set it relative to the end of the file.
#
# how − This is the reference point with-in the file. os.SEEK_SET or 0 means beginning of the file, os.SEEK_CUR or 1 means the current position and os.SEEK_END or 2 means end of the file.
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

# Now you can use fsync() method.
# Infact here you would not be able to see its effect.
os.fsync(fd)

# Now read this file from the beginning
os.lseek(fd, 0, 0)
str = os.read(fd, 100)
print("Read String is : ", str)

# Close opened file
os.close(fd)

print("Closed the file successfully!!")
