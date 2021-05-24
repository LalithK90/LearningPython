# Description
#
# The method fpathconf() returns system configuration information relevant to an open file.This variable is very similar to unix system call fpathconf() and accept the similar arguments.
# Syntax
#
# Following is the syntax for fpathconf() method −
#
# os.fpathconf(fd, name)
#
# Parameters
#
# fd − This is the file descriptor for which system configuration information is to be returned.
#
# name − This specifies the configuration value to retrieve; it may be a string, which is the name of a defined system value; these names are specified in a number of standards (POSIX.1, Unix 95, Unix 98, and others). The names known to the host operating system are given in the os.pathconf_names dictionary.
#
# Return Value
#
# This method returns system configuration information relevant to an open file.
# Example
import os, sys

# Open a file
fd = os.open("foo.txt", os.O_RDWR | os.O_CREAT)

print("%s" % os.pathconf_names)

# Now get maximum number of links to the file.
no = os.fpathconf(fd, 'PC_LINK_MAX')
print("Maximum number of links to the file. :%d" % no)

# Now get maximum length of a filename
no = os.fpathconf(fd, 'PC_NAME_MAX')
print("Maximum length of a filename :%d" % no)

# Close opened file
os.close(fd)

print("Closed the file successfully!!")
