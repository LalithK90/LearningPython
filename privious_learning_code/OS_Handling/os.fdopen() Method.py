# Description
#
# The method fdopen() returns an open file object connected to the file descriptor fd. Then you can perform all the defined functions on file object.
# Syntax
#
# Following is the syntax for fdopen() method −
#
# os.fdopen(fd, [, mode[, bufsize]]);
#
# Parameters
#
# fd − This is the file descriptor for which a file object is to be returned.
#
# mode − This optional argument is a string indicating how the file is to be opened. The most commonly-used values of mode are 'r' for reading, 'w' for writing (truncating the file if it already exists), and 'a' for appending.
#
# bufsize − This optional argument specifies the file's desired buffer size: 0 means unbuffered, 1 means line buffered, any other positive value means use a buffer of (approximately) that size.
#
# Return Value
#
# This method returns an open file object connected to the file descriptor.
# Example
import os, sys

# Open a file
fd = os.open("foo.txt", os.O_RDWR | os.O_CREAT)

# Now get a file object for the above file.
fo = os.fdopen(fd, "w+")

# Tell the current position
print("Current I/O pointer position :%d" % fo.tell())

# Write one string
fo.write("Python is a great language.\nYeah its great!!\n")

# Now read this file from the beginning.
os.lseek(fd, 0, 0)
str = os.read(fd, 100)
print("Read String is : ", str)

# Tell the current position
print("Current I/O pointer position :%d" % fo.tell())

# Close opened file
fo.close()

print("Closed the file successfully!!")
