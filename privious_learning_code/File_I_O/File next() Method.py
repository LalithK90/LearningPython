# Description
#
# The method next() is used when a file is used as an iterator, typically in a loop, the next() method is called repeatedly. This method returns the next input line, or raises StopIteration when EOF is hit.
#
# Combining next() method with other file methods like readline() does not work right. However, usingseek() to reposition the file to an absolute position will flush the read-ahead buffer.
# Syntax
#
# Following is the syntax for next() method −
#
# fileObject.next();
#
# Parameters
#
# NA
#
# Return Value
#
# This method returns the next input line.
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

for index in range(5):
line = fo.next()
print("Line No %d - %s" % (index, line))

# Close opend file
fo.close()
