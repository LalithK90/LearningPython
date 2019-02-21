
# Description
#
# The method stat() performs a stat system call on the given path.
# Syntax
#
# Following is the syntax for stat() method −
#
# os.stat(path)
#
# Parameters
#
#     path − This is the path, whose stat information is required.
#
# Return Value
#
# Here is the list of members of stat structure −
#
#     st_mode − protection bits.
#
#     st_ino − inode number.
#
#     st_dev − device.
#
#     st_nlink − number of hard links.
#
#     st_uid − user id of owner.
#
#     st_gid − group id of owner.
#
#     st_size − size of file, in bytes.
#
#     st_atime − time of most recent access.
#
#     st_mtime − time of most recent content modification.
#
#     st_ctime − time of most recent metadata change.
#
# Example
import os, sys

# showing stat information of file "a2.py"
statinfo = os.stat('a2.py')

print(statinfo)