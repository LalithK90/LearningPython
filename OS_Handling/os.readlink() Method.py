# Description
#
# The method readlink() returns a string representing the path to which the symbolic link points. It may return an absolute or relative pathname.
# Syntax
#
# Following is the syntax for readlink() method −
#
# os.readlink(path)
#
# Parameters
#
#     path − This is the path or symblic link for which we are going to find source of the link.
#
# Return Value
#
# This method return a string representing the path to which the symbolic link points.
# Example
import os

src = '/usr/bin/python'
dst = '/tmp/python'

# This creates a symbolic link on python in tmp directory
os.symlink(src, dst)

# Now let us use readlink to display the source of the link.
path = os.readlink(dst)
print(path)
