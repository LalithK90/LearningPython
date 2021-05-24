
# Description
#
# The method lchmod() changes the mode of path to the numeric mode. If path is a symlink, this affects the symlink rather than the target.
#
# The mode may take one of the following values or bitwise ORed combinations of them −
#
# stat.S_ISUID − Set user ID on execution.
#
# stat.S_ISGID − Set group ID on execution.
#
# stat.S_ENFMT − Record locking enforced.
#
# stat.S_ISVTX − Save text image after execution.
#
# stat.S_IREAD − Read by owner.
#
# stat.S_IWRITE − Write by owner.
#
# stat.S_IEXEC − Execute by owner.
#
# stat.S_IRWXU − Read, write, and execute by owner.
#
# stat.S_IRUSR − Read by owner.
#
# stat.S_IWUSR − Write by owner.
#
# stat.S_IXUSR − Execute by owner.
#
# stat.S_IRWXG − Read, write, and execute by group.
#
# stat.S_IRGRP − Read by group.
#
# stat.S_IWGRP − Write by group.
#
# stat.S_IXGRP − Execute by group.
#
# stat.S_IRWXO − Read, write, and execute by others.
#
# stat.S_IROTH − Read by others.
#
# stat.S_IWOTH − Write by others.
#
# stat.S_IXOTH − Execute by others.
#
# Note −This method has been introduced in Python 2.6
# Syntax
#
# Following is the syntax for lchmod() method −
#
# os.lchmod(path, mode)
#
# Parameters
#
# path − This is the file path for which mode to be set.
#
# mode − This may take one of the above mentioned values or bitwise ORed combinations of them.
#
# Return Value
#
# This method does not return any value.
# Example
import os, sys

# Open a file
import stat

path = "/var/www/html/foo.txt"
fd = os.open( path, os.O_RDWR|os.O_CREAT )

# Close opened file
os.close( fd )

# Now change the file mode.
# Set a file execute by group.
os.lchmod( path, stat.S_IXGRP)

# Set a file write by others.
os.lchmod("/tmp/foo.txt", stat.S_IWOTH)

print("Changed mode successfully!!")