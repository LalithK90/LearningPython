
# Description
#
# The method renames() is recursive directory or file renaming function. It does the same functioning as os.rename(), but it also moves a file to a directory, or a whole tree of directories, that do not exist.
# Syntax
#
# Following is the syntax for renames() method −
#
# os.renames(old, new)
#
# Parameters
#
# old − This is the actual name of the file or directory to be renamed.
#
# new − This is the new name of the file or directory.It can even include a file to a directory, or a whole tree of directories, that do not exist.
#
# Return Value
#
# This method does not return any value.
# Example
import os, sys
print("Current directory is: %s" %os.getcwd())

# listing directories
print("The dir is: %s"%os.listdir(os.getcwd()))

# renaming file "aa1.txt"
os.renames("aa1.txt","newdir/aanew.txt")

print("Successfully renamed.")

# listing directories after renaming and moving "aa1.txt"
print("The dir is: %s" %os.listdir(os.getcwd()))