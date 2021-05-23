
# Description
#
# The method readline()reads one entire line from the file. A trailing newline character is kept in the string. If the size argument is present and non-negative, it is a maximum byte count including the trailing newline and an incomplete line may be returned.
#
# An empty string is returned only when EOF is encountered immediately.
# Syntax
#
# Following is the syntax for readline() method −
#
# fileObject.readline( size );
#
# Parameters
#
#     size − This is the number of bytes to be read from the file.
#
# Return Value
#
# This method returns the line read from the file.
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

line = fo.readline()
print("Read Line: %s" % (line))

line = fo.readline(5)
print("Read Line: %s" % (line))

# Close opend file
fo.close()