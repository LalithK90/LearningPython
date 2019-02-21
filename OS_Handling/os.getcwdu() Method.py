
# Description
#
# The method getcwdu() returns a unicode object representing the current working directory.
# Syntax
#
# Following is the syntax for getcwdu() method −
#
# os.getcwdu()
#
# Parameters
#
#     NA
#
# Return Value
#
# This method returns a unicode object representing the current working directory.
# Example
import os, sys

# First go to the "/var/www/html" directory
os.chdir("/var/www/html" )

# Print current working directory
print("Current working dir : %s" % os.getcwdu())

# Now open a directory "/tmp"
fd = os.open( "/tmp", os.O_RDONLY )

# Use os.fchdir() method to change the dir
os.fchdir(fd)

# Print current working directory
print("Current working dir : %s" % os.getcwdu())

# Close opened directory.
os.close( fd )