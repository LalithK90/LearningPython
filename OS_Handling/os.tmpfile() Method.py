
# Description
#
# The method tmpfile() returns a new temporary file object opened in update mode (w+b). The file has no directory entries associated with it and will be deleted automatically once there are no file descriptors.
# Syntax
#
# Following is the syntax for tmpfile() method −
#
# os.tmpfile
#
# Parameters
#
#     NA
#
# Return Value
#
# This method returns a new temporary file object
# Example
import os

# The file has no directory entries associated with it and will be
# deleted automatically once there are no file descriptors.
tmpfile = os.tmpfile()
tmpfile.write('Temporary newfile is here.....')
tmpfile.seek(0)

print(tmpfile.read())
tmpfile.close