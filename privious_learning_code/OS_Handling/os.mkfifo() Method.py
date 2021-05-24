
# Description
#
# The method mkfifo() create a FIFO named path with numeric mode. The default mode is 0666 (octal).The current umask value is first masked out.
# Syntax
#
# Following is the syntax for mkfifo() method −
#
# os.mkfifo(path[, mode])
#
# Parameters
#
# path − This is the path, which needs to be created.
#
# mode − This is the mode of the named path to be given.
#
# Return Value
#
# This method does not return any value.
# Example
import os, sys

# Path to be created
path = "/tmp/hourly"

os.mkfifo(path, 0o644)

print("Path is created")