
# Description
#
# The method symlink() creates a symbolic link dst pointing to src.
# Syntax
#
# Following is the syntax for symlink() method −
#
# os.symlink(src, dst)
#
# Parameters
#
#     src − This is the source.
#
#     dest − This is the destination, which didn't exist previously.
#
# Return Value
#
# This method does not return any value.
# Example
import os

src = '/usr/bin/python'
dst = '/tmp/python'

# This creates a symbolic link on python in tmp directory
os.symlink(src, dst)

print("symlink created")