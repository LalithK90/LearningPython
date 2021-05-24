
# Description
#
# The method fstatvfs() returns information about the file system containing the file associated with file descriptor fd. This returns the following sturcture −
#
# f_bsize − file system block size
#
# f_frsize − fragment size
#
# f_blocks − size of fs in f_frsize units
#
# f_bfree − free blocks
#
# f_bavail − free blocks for non-root
#
# f_files − inodes
#
# f_ffree − free inodes
#
# f_favail − free inodes for non-root
#
# f_fsid − file system ID
#
# f_flag − mount flags
#
# f_namemax − maximum filename length
#
# Syntax
#
# Following is the syntax for fstatvfs() method −
#
# os.fstatvfs(fd)
#
# Parameters
#
# fd − This is the file descriptor for which system information is to be returned.
#
# Return Value
#
# This method returns information about the file system containing the file associated.
# Example
import os, sys

# Open a file
fd = os.open( "foo.txt", os.O_RDWR|os.O_CREAT )

# Now get  the touple
info = os.fstatvfs(fd)

print("File Info :", info)

# Now get maximum filename length
print('Maximum filename length :%d' % info.f_namemax:)

# Now get free blocks
print("Free blocks :%d" % info.f_bfree)

# Close opened file
os.close( fd)