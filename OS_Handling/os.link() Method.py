
# Description
#
# The method link() creates a hard link pointing to src named dst. This method is very useful to create a copy of existing file.
# Syntax
#
# Following is the syntax for link() method −
#
# os.link(src, dst)
#
# Parameters
#
#     src − This is the source file path for which hard link would be created.
#
#     dest − This is the target file path where hard link would be created.
#
# Return Value
#
# This method does not return any value.
# Example
import os, sys

# Open a file
path = "/var/www/html/foo.txt"
fd = os.open( path, os.O_RDWR|os.O_CREAT )

# Close opened file
os.close( fd )

# Now create another copy of the above file.
dst = "/tmp/foo.txt"
os.link( path, dst)

print("Created hard link successfully!!")