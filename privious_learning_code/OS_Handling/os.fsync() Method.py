# Description
#
# The method fsync() forces write of file with file descriptor fd to disk. If you're starting with a Python file object f, first do f.flush(), and then do os.fsync(f.fileno()), to ensure that all internal buffers associated with f are written to disk.
# Syntax
#
# Following is the syntax for fsync() method −
#
# os.fsync(fd)
#
# Parameters
#
#     fd − This is the file descriptor for buffer sync is required.
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
