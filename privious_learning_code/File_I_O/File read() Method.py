
# Description
#
# The method read() reads at most size bytes from the file. If the read hits EOF before obtaining size bytes,
# then it reads only available bytes. Syntax
#
# Following is the syntax for read() method −
#
# fileObject.read( size );
#
# Parameters
#
# size − This is the number of bytes to be read from the file.
#
# Return Value
#
# This method returns the bytes read in string.
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

line = fo.read(10)
print("Read Line: %s" % (line))

# Close opend file
fo.close()