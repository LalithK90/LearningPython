
# Description
#
# The method lstat() is very similar to fstat() and returns the information about a file, but do not follow symbolic links. This is an alias for fstat() on platforms that do not support symbolic links, such as Windows.
#
# Here is the structure returned by lstat method −
#
# st_dev − ID of device containing file
#
# st_ino − inode number
#
# st_mode − protection
#
# st_nlink − number of hard links
#
# st_uid − user ID of owner
#
# st_gid − group ID of owner
#
# st_rdev − device ID (if special file)
#
# st_size − total size, in bytes
#
# st_blksize − blocksize for filesystem I/O
#
# st_blocks − number of blocks allocated
#
# st_atime − time of last access
#
# st_mtime − time of last modification
#
# st_ctime − time of last status change
#
# Syntax
#
# Following is the syntax for lstat() method −
#
# os.lstat(path)
#
# Parameters
#
# path − This is the file for which information would be returned.
#
# Return Value
#
# This method returns the information about a file.
# Example
import os, sys

# Open a file
path = "/var/www/html/foo.txt"
fd = os.open( path, os.O_RDWR|os.O_CREAT )

# Close opened file
os.close( fd )

# Now get  the touple
info = os.lstat(path)

print("File Info :", info)

# Now get uid of the file
print("UID of the file :%d" % info.st_uid)

# Now get gid of the file
print("GID of the file :%d" % info.st_gid)