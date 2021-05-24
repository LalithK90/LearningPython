
# Description
#
# The method fstat() returns information about a file associated with the fd. Here is the structure returned by fstat method −
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
# Following is the syntax for fstat() method −
#
# os.fstat(fd)
#
# Parameters
#
# fd − This is the file descriptor for which system information is to be returned.
#
# Return Value
#
# This method returns information about a file associated with the fd.
# Example
import os, sys

# Open a file
fd = os.open( "foo.txt", os.O_RDWR|os.O_CREAT )

# Now get  the touple
info = os.fstat(fd)

print("File Info :", info)

# Now get uid of the file
print("UID of the file :%d" % info.st_uid)

# Now get gid of the file
print("GID of the file :%d" % info.st_gid)

# Close opened file
os.close( fd)