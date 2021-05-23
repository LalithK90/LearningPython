
# Description
#
# The method pathconf() returns system configuration information relevant to a named file.
# Syntax
#
# Following is the syntax for pathconf() method −
#
# os.pathconf(path, name)
#
# Parameters
#
#     path − This is the file path.
#
#     name − This specifies the configuration value to retrieve; it may be a string which is the name of a defined system value; these names are specified in a number of standards (POSIX.1, Unix 95, Unix 98, and others). The names known to the host operating system are given in the os.pathconf_names dictionary.
#
# Return Value
#
# This method returns system configuration information of a file.
# Example
import os, sys

print("%s" % os.pathconf_names)

# Retrieve maximum length of a filename
no = os.pathconf('a2.py', 'PC_NAME_MAX')
print("Maximum length of a filename :%d" % no)

# Retrieve file size
no = os.pathconf('a2.py', 'PC_FILESIZEBITS')
print("file size in bits  :%d" % no)