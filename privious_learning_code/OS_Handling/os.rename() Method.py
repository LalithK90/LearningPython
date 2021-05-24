# Description
#
# The method rename() renames the file or directory src to dst.If dst is a file or directory(already present), OSError will be raised.
# Syntax
#
# Following is the syntax for rename() method −
#
# os.rename(src, dst)
#
# Parameters
#
# src − This is the actual name of the file or directory.
#
# dst − This is the new name of the file or directory.
#
# Return Value
#
# This method does not return any value.
# Example
import os, sys

# listing directories
print("The dir is: %s" % os.listdir(os.getcwd()))

# renaming directory ''tutorialsdir"
os.rename("tutorialsdir", "tutorialsdirectory")

print("Successfully renamed.")

# listing directories after renaming "tutorialsdir"
print("the dir is: %s" % os.listdir(os.getcwd()))
