# Description
#
# The method getcwd() returns current working directory of a process.
# Syntax
#
# Following is the syntax for getcwd() method −
#
# cwd = os.getcwd()
#
# Parameters
#
# NA
#
# Return Value
#
# This method returns current working directory of a process.
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
