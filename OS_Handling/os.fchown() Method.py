# Description
#
# The method fchown() changes the owner and group id of the file given by fd to the numeric uid and gid. To leave one of the ids unchanged, set it to -1.
#
# Note −This method is available Python 2.6 onwards.
# Syntax
#
# Following is the syntax for fchown() method −
#
# os.fchown(fd, uid, gid);
#
# Parameters
#
#     fd − This is the file descriptor for which owner id and group id need to be set up.
#
#     uid − This is Owner ID to be set for the file.
#
#     gid − This is Group ID to be set for the file.
#
# Return Value
#
# This method does not return any value.
# Example
import os, sys, stat

# Now open a file "/tmp/foo.txt"
fd = os.open("/tmp", os.O_RDONLY)

# Set the user Id to 100 for this file.
os.fchown(fd, 100, -1)

# Set the group Id to 50 for this file.
os.fchown(fd, -1, 50)

print("Changed ownership successfully!!")

# Close opened file.
os.close(fd)
