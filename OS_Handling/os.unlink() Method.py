
# Description
#
# The method unlink() removes (deletes) the file path.If the path is a directory, OSError is raised.
# Syntax
#
# Following is the syntax for unlink() method −
#
# os.unlink(path)
#
# Parameters
#
#     path − This is the path, which is to be removed.
#
# Return Value
#
# This method does not return any value.
# Example
import os, sys

# listing directories
print("The dir is: %s" %os.listdir(os.getcwd()))

os.unlink("aa.txt")

# listing directories after removing path
print("The dir after removal of path : %s" %os.listdir(os.getcwd()))