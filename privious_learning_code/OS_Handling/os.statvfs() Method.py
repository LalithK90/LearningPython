
# Description
#
# The method statvfs() perform a statvfs system call on the given path.
# Syntax
#
# Following is the syntax for statvfs() method −
#
# os.statvfs(path)
#
# Parameters
#
# path − This is the path, whose statvfs information is required.
#
# Return Value
#
# Here is the list of members of statvfs structure −
#
# f_bsize − preferred file system block size.
#
# f_frsize − fundamental file system block size.
#
# f_blocks − total number of blocks in the filesystem.
#
# f_bfree − total number of free blocks.
#
# f_bavail − free blocks available to non-super user.
#
# f_files − total number of file nodes.
#
# f_ffree − total number of free file nodes.
#
# f_favail − free nodes available to non-super user.
#
# f_flag − system dependent.
#
# f_namemax − maximum file name length.
#
# Example
import os, sys

# showing statvfs information of file "a1.py"
stinfo = os.statvfs('a1.py')

print(stinfo)