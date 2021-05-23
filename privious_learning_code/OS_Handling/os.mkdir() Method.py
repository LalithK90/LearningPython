
# Description
#
# The method mkdir() create a directory named path with numeric mode mode. The default mode is 0777 (octal). On some systems, mode is ignored. Where it is used, the current umask value is first masked out.
# Syntax
#
# Following is the syntax for mkdir() method −
#
# os.mkdir(path[, mode])
#
# Parameters
#
#     path − This is the path, which needs to be created.
#
#     mode − This is the mode of the directories to be given.
#
# Return Value
#
# This method does not return any value.
# Example
import os, sys

# Path to be created
path = "/tmp/home/monthly/daily/hourly"

os.mkdir(path, 0o755)

print("Path is created")