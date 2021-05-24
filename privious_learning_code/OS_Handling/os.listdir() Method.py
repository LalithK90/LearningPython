# Description
#
# The method listdir() returns a list containing the names of the entries in the directory given by path. The list is in arbitrary order. It does not include the special entries '.' and '..' even if they are present in the directory.
# Syntax
#
# Following is the syntax for listdir() method −
#
# os.listdir(path)
#
# Parameters
#
# path − This is the directory, which needs to be explored.
#
# Return Value
#
# This method returns a list containing the names of the entries in the directory given by path.
# Example
import os, sys

# Open a file
path = "/var/www/html/"
dirs = os.listdir(path)

# This would print all the files and directories
for file in dirs:
print(file)
