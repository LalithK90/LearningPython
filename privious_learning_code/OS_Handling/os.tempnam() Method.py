
# Description
#
# The method tempnam() returns a unique path name that is reasonable for creating a temporary file.
# Syntax
#
# Following is the syntax for tempnam() method −
#
# os.tempnam(dir, prefix)
#
# Parameters
#
# dir − This is the dir where the temporary filename will be created.
#
# prefix − This is the prefix of the generated temporary filename.
#
# Return Value
#
# This method returns a unique path.
# Example
import os, sys

# prefix is tuts1 of the generated file
tmpfn = os.tempnam('/tmp/dir,'tut')

print("This is the unique path:")
print(tmpfn)