
# Description
#
# The method truncate() truncates the file's size. If the optional size argument is present, the file is truncated to (at most) that size.
#
# The size defaults to the current position. The current file position is not changed. Note that if a specified size exceeds the file's current size, the result is platform-dependent.
#
# Note − This method would not work in case file is opened in read-only mode.
# Syntax
#
# Following is the syntax for truncate() method −
#
# fileObject.truncate( [ size ])
#
# Parameters
#
#     size − If this optional argument is present, the file is truncated to (at most) that size.
#
# Return Value
#
# This method does not return any value.
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

# Now truncate remaining file.
fo.truncate()

# Try to read file now
line = fo.readline()
print("Read Line: %s" % (line))

# Close opend file
fo.close()