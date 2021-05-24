# Description
#
# The method fchdir() change the current working directory to the directory represented by the file descriptor fd. The descriptor must refer to an opened directory, not an open file.
# Syntax
#
# Following is the syntax for fchdir() method −
#
# os.fchdir(fd);
#
# Parameters
#
# fd − This is Directory descriptor.
#
# Return Value
#
# This method does not return any value.
# Example
import os, sys

# First go to the "/var/www/html" directory
os.chdir("/var/www/html")

# Print current working directory
print("Current working dir : %s" % os.getcwd())

# Now open a directory "/tmp"
fd = os.open("/tmp", os.O_RDONLY)

# Use os.fchdir() method to change the dir
os.fchdir(fd)

# Print current working directory
print("Current working dir : %s" % os.getcwd())

# Close opened directory.
os.close(fd)
