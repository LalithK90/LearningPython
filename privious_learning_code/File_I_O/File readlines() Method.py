
# Description
#
# The method readlines() reads until EOF using readline() and returns a list containing the lines. If the optional sizehint argument is present, instead of reading up to EOF, whole lines totalling approximately sizehint bytes (possibly after rounding up to an internal buffer size) are read.
#
# An empty string is returned only when EOF is encountered immediately.
# Syntax
#
# Following is the syntax for readlines() method −
#
# fileObject.readlines( sizehint );
#
# Parameters
#
# sizehint − This is the number of bytes to be read from the file.
#
# Return Value
#
# This method returns a list containing the lines.
# Example
# Open a file
fo = open("foo.txt", "rw+")
print("Name of the file: ", fo.name)

# Assuming file has following 5 lines
# This is 1st line
# This is 2nd line
# This is 3rd line
# This is 4th line
# This is 5th line

line = fo.readlines()
print("Read Line: %s" % (line))

line = fo.readlines(2)
print("Read Line: %s" % (line))

# Close opend file
fo.close()