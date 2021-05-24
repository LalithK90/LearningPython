
# Description
#
# The method chown() changes the owner and group id of path to the numeric uid and gid. To leave one of the ids
# unchanged, set it to -1.To set ownership, you would need super user privilege.. Syntax
#
# Following is the syntax for chown() method −
#
# os.chown(path, uid, gid);
#
# Parameters
#
# path − This is the path for which owner id and group id need to be setup.
#
# uid − This is Owner ID to be set for the file.
#
# gid − This is Group ID to be set for the file.
#
# Return Value
#
# This method does not return any value.
# Example
import os, sys

# Assuming /tmp/foo.txt exists.
# To set owner ID 100 following has to be done.
os.chown("/tmp/foo.txt", 100, -1)

print("Changed ownership successfully!!")