
# Description
#
# The method lchflags() sets the flags of path to the numeric flags. This method does not follow symbolic links unlike chflags() method.
#
# Here, flags may take a combination (bitwise OR) of the following values (as defined in the stat module) −
#
#     UF_NODUMP − Do not dump the file.
#
#     UF_IMMUTABLE − The file may not be changed.
#
#     UF_APPEND − The file may only be appended to.
#
#     UF_NOUNLINK − The file may not be renamed or deleted.
#
#     UF_OPAQUE − The directory is opaque when viewed through a union stack.
#
#     SF_ARCHIVED − The file may be archived.
#
#     SF_IMMUTABLE − The file may not be changed.
#
#     SF_APPEND − The file may only be appended to.
#
#     SF_NOUNLINK − The file may not be renamed or deleted.
#
#     SF_SNAPSHOT − The file is a snapshot file.
#
# Note − This method has been introduced in Python 2.6
# Syntax
#
# Following is the syntax for lchflags() method −
#
# os.lchflags(path, flags)
#
# Parameters
#
#     path − This is the file path for which flags to be set.
#
#     flags − This could be a combination (bitwise OR) of the above defined flags values.
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

# Now change the file flag.
ret = os.lchflags(path, os.UF_IMMUTABLE )

print("Changed file flag successfully!!")