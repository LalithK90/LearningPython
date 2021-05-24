# Description
#
# The method open() opens the file file and set various flags according to flags and possibly its mode according to mode.The default mode is 0777 (octal), and the current umask value is first masked out.
# Syntax
#
# Following is the syntax for open() method −
#
# os.open(file, flags[, mode]);
#
# Parameters
#
# file − File name to be opened.
#
# flags − The following constants are options for the flags. They can be combined using the bitwise OR operator |. Some of them are not available on all platforms.
#
# os.O_RDONLY − open for reading only
#
# os.O_WRONLY − open for writing only
#
# os.O_RDWR − open for reading and writing
#
# os.O_NONBLOCK − do not block on open
#
# os.O_APPEND − append on each write
#
# os.O_CREAT − create file if it does not exist
#
# os.O_TRUNC − truncate size to 0
#
# os.O_EXCL − error if create and file exists
#
# os.O_SHLOCK − atomically obtain a shared lock
#
# os.O_EXLOCK − atomically obtain an exclusive lock
#
# os.O_DIRECT − eliminate or reduce cache effects
#
# os.O_FSYNC − synchronous writes
#
# os.O_NOFOLLOW − do not follow symlinks
#
# mode − This work in similar way as it works for chmod() method.
#
# Return Value
#
# This method returns the file descriptor for the newly opened file.
# Example
import os, sys

# Open a file
fd = os.open("foo.txt", os.O_RDWR | os.O_CREAT)

# Write one string
os.write(fd, "This is test")

# Close opened file
os.close(fd)

print("Closed the file successfully!!")
