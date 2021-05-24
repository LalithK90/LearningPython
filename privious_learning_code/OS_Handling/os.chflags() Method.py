
# Description
#
# The method chflags() sets the flags of path to the numeric flags. The flags may take a combination (bitwise OR) of the various values described below.
#
# Note − This method is available Python version 2.6 onwards. Most of the flags can be changed by super-user only.
# Syntax
#
# Following is the syntax for chflags() method −
#
# os.chflags(path, flags)
#
# Parameters
#
# path − This is complete path of the directory to be changed to a new location.
#
# flags − The flags specified are formed by OR'ing the following values −
#
# so.UF_NODUMP − Do not dump the file.
#
# so.UF_IMMUTABLE − The file may not be changed.
#
# so.UF_APPEND − The file may only be appended to.
#
# so.UF_NOUNLINK − The file may not be renamed or deleted.
#
# so.UF_OPAQUE − The directory is opaque when viewed through a union stack.
#
# so.SF_ARCHIVED − The file may be archived.
#
# so.SF_IMMUTABLE − The file may not be changed.
#
# so.SF_APPEND − The file may only be appended to.
#
# so.SF_NOUNLINK − The file may not be renamed or deleted.
#
# so.SF_SNAPSHOT − The file is a snapshot file.
#
# Return Value
#
# This method does not return any value.
# Example
import os
import stat

path = "/tmp/foo.txt"

# Set a flag so that file may not be renamed or deleted.
flags = os.SF_NOUNLINK
retval = os.chflags( path, flags)
print("Return Value: %s" % retval)