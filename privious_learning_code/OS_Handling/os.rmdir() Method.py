
# Description
#
# The method rmdir() removes the directory path. It works only when the directory is empty, else OSError is raised.
# Syntax
#
# Following is the syntax for rmdir() method −
#
# os.rmdir(path)
#
# Parameters
#
# path − This is the path of the directory, which needs to be removed.
#
# Return Value
#
# This method does not return any value.
# Example
# listing directories
import os

print("the dir is: %s" %os.listdir(os.getcwd()))

# removing path
os.rmdir("mydir")

# listing directories after removing directory path
print("the dir is:" %os.listdir(os.getcwd()))