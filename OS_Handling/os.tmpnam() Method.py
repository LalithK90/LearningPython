
# Description
#
# The method tmpnam() returns a unique path name that is reasonable for creating a temporary file.
# Syntax
#
# Following is the syntax for tmpnam() method −
#
# os.tmpnam()
#
# Parameters
#
#     NA
#
# Return Value
#
# This method returns a unique path name.
# Example
import os, sys

# Temporary file generated in current directory
tmpfn = os.tmpnam()

print("This is the unique path:")
print(tmpfn)