
# Description
#
# The method removedirs() removes dirs recursively. If the leaf directory is succesfully removed, removedirs tries to successively remove every parent directory displayed in path.
# Syntax
#
# Following is the syntax for removedirs() method −
#
# os.removedirs(path)
#
# Parameters
#
#     path − This is the path of the directory, which needs to be removed.
#
# Return Value
#
# This method does not return any value.
# Example
import os, sys

# listing directories
print("The dir is: %s" %os.listdir(os.getcwd()))

# removing
os.removedirs("/tutorialsdir")

# listing directories after removing directory
print("The dir after removal is:" %os.listdir(os.getcwd()))