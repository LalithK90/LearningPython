# Description
#
# The method lchown() changes the owner and group id of path to the numeric uid and gid. This function will not follow symbolic links. To leave one of the ids unchanged, set it to -1. .
# Syntax
#
# Following is the syntax for lchown() method −
#
# os.lchown(path, uid, gid)
#
# Parameters
#
#     path − This is the file path for which ownership to be set.
#
#     uid − This is the Owner ID to be set for the file.
#
#     gid − This is the Group ID to be set for the file.
#
# Return Value
#
# This method does not return any value.
# Example
import os, sys

# Open a file
path = "/var/www/html/foo.txt"
fd = os.open(path, os.O_RDWR | os.O_CREAT)

# Close opened file
os.close(fd)

# Now change the file ownership.
# Set a file owner ID
os.lchown(path, 500, -1)

# Set a file group ID
os.lchown(path, -1, 500)

print("Changed ownership successfully!!")
