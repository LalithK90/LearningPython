
# Description
#
# The method mknod() creates a filesystem node (file, device special file or named pipe) named filename.
# Syntax
#
# Following is the syntax for mknod() method −
#
# os.mknod(filename[, mode=0600[, device=0]])
#
# Parameters
#
#     filename − This is the filesystem node to be created.
#
#     mode − The mode specifies both the permissions to use and the type of node to be created combined (bitwise OR) with one of the values stat.S_IFREG, stat.S_IFCHR, stat.S_IFBLK, and stat.S_IFIFO. They can be ORed base don requirement.
#
#     device − This is the device special file created and its optional to provide.
#
# Return Value
#
# This method does not return any value.
# Example
import os
import stat

filename = '/tmp/tmpfile'
mode = 0o600 | stat.S_IRUSR

# filesystem node specified with different modes
os.mknod(filename, mode)