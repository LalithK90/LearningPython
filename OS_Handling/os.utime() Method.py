
# Description
#
# The method utime() sets the access and modified times of the file specified by path.
# Syntax
#
# Following is the syntax for utime() method −
#
# os.utime(path, times)
#
# Parameters
#
#     path − This is the path of the file.
#
#     times − This is the file access and modified time. If times is none, then the file access and modified times are set to the current time. The parameter times consists of row in the form of (atime, mtime) i.e (accesstime, modifiedtime).
#
# Return Value
#
# This method does not return any value.
# Example
import os, sys

# Showing stat information of file
stinfo = os.stat('a2.py')
print(stinfo)

# Using os.stat to recieve atime and mtime of file
print("access time of a2.py: %s" %stinfo.st_atime)
print("modified time of a2.py: %s" %stinfo.st_mtime)

# Modifying atime and mtime
os.utime("a2.py",(1330712280, 1330712292))
print("done!!")