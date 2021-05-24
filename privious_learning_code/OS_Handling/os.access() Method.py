
# Description
#
# The method access() uses the real uid/gid to test for access to path. Most operations will use the effective uid/gid, therefore this routine can be used in a suid/sgid environment to test if the invoking user has the specified access to path.It returns True if access is allowed, False if not.
# Syntax
#
# Following is the syntax for access() method −
#
# os.access(path, mode);
#
# Parameters
#
# path − This is the path which would be tested for existence or any access.
#
# mode − This should be F_OK to test the existence of path, or it can be the inclusive OR of one or more of R_OK, W_OK, and X_OK to test permissions.
# os.F_OK − Value to pass as the mode parameter of access() to test the existence of path.
# os.R_OK − Value to include in the mode parameter of access() to test the readability of path.
# os.W_OK Value to include in the mode parameter of access() to test the writability of path.
# os.X_OK Value to include in the mode parameter of access() to determine if path can be executed.
#
# Return Value
#
# This method returns True if access is allowed, False if not.
# Example
import os, sys

# Assuming /tmp/foo.txt exists and has read/write permissions.

ret = os.access("/tmp/foo.txt", os.F_OK)
print("F_OK - return value %s"% ret)

ret = os.access("/tmp/foo.txt", os.R_OK)
print("R_OK - return value %s"% ret)

ret = os.access("/tmp/foo.txt", os.W_OK)
print("W_OK - return value %s"% ret)

ret = os.access("/tmp/foo.txt", os.X_OK)
print("X_OK - return value %s"% ret)