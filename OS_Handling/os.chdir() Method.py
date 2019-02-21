
# Description
#
# The method chdir() changes the current working directory to the given path.It returns None in all the cases.
# Syntax
#
# Following is the syntax for chdir() method −
#
# os.chdir(path)
#
# Parameters
#
#     path − This is complete path of the directory to be changed to a new location.
#
# Return Value
#
# This method does not return any value.
# Example
import os

path = "/usr/tmp"

# Check current working directory.
retval = os.getcwd()
print("Current working directory %s" % retval)

# Now change the directory
os.chdir( path )

# Check current working directory.
retval = os.getcwd()

print("Directory changed successfully %s" % retval)