
# Description
#
# The method fdatasync() forces write of file with filedescriptor fd to disk. This does not force update of metadata. If you want to flush your buffer then you can use this method.
# Syntax
#
# Following is the syntax for fdatasync() method −
#
# os.fdatasync(fd);
#
# Parameters
#
#     fd − This is the file descriptor for which data to be written.
#
# Return Value
#
# This method does not return any value.
# Example
import os, sys

# Open a file
fd = os.open( "foo.txt", os.O_RDWR|os.O_CREAT )

# Write one string
os.write(fd, "This is test")

# Now you can use fdatasync() method.
# Infact here you would not be able to see its effect.
os.fdatasync(fd)

# Now read this file from the beginning.
os.lseek(fd, 0, 0)
str = os.read(fd, 100)
print("Read String is : ", str)

# Close opened file
os.close( fd )

print("Closed the file successfully!!")