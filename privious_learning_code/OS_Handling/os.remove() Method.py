
# Description
#
# The method remove() removes the file path. If the path is a directory, OSError is raised.
# Syntax
#
# Following is the syntax for remove() method −
#
# os.remove(path)
#
# Parameters
#
# path − This is the path, which is to be removed.
#
# Return Value
#
# This method does not return any value.
# Example
import os, sys

# listing directories
print("The dir is: %s" %os.listdir(os.getcwd()))

# removing
os.remove("aa.txt")

# listing directories after removing path
print("The dir after removal of path : %s" %os.listdir(os.getcwd()))