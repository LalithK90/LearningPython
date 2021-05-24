# Description
#
# The method fchmod() changes the mode of the file given by fd to the numeric mode. The mode may take one of the following values or bitwise ORed combinations of them −
#
# Note − This method is available Python 2.6 onwards.
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
# Syntax
#
# Following is the syntax for fchmod() method −
#
# os.fchmod(fd, mode);
#
# Parameters
#
# fd − This is the file descriptor for which mode would be set.
#
# mode − This may take one of the above mentioned values or bitwise ORed combinations of them.
#
# Return Value
#
# This method does not return any value.
# Example
import os, sys, stat

# Now open a file "/tmp/foo.txt"
fd = os.open("/tmp", os.O_RDONLY)

# Set a file execute by the group.

os.fchmod(fd, stat.S_IXGRP)

# Set a file write by others.
os.fchmod(fd, stat.S_IWOTH)

print("Changed mode successfully!!")

# Close opened file.
os.close(fd)
