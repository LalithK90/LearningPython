
# Description
#
# The method makedirs() is recursive directory creation function. Like mkdir(), but makes all intermediate-level directories needed to contain the leaf directory.
# Syntax
#
# Following is the syntax for makedirs() method −
#
# os.makedirs(path[, mode])
#
# Parameters
#
#     path − This is the path, which needs to be created recursively.
#
#     mode − This is the Mode of the directories to be given.
#
# Return Value
#
# This method does not return any value.
# Example
import os, sys

# Path to be created
path = "/tmp/home/monthly/daily"

os.makedirs( path, 0755 );

print("Path is created")