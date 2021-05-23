
# Description
#
# The method chroot() changes the root directory of the current process to the given path.To use this method, you would need super user privilege.
# Syntax
#
# Following is the syntax for chroot() method −
#
# os.chroot(path);
#
# Parameters
#
#     path − This is the path which would be set as root for the current process.
#
# Return Value
#
# This method does not return any value.
# Example
import os, sys

# To set the current root path to /tmp/user
os.chroot("/tmp/usr")
print("Changed root path successfully!!")