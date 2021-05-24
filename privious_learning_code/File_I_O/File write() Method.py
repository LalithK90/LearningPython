# Description
#
# The method write() writes a string str to the file. There is no return value. Due to buffering, the string may not actually show up in the file until the flush() or close() method is called.
# Syntax
#
# Following is the syntax for write() method −
#
# fileObject.write( str )
#
# Parameters
#
# str − This is the String to be written in the file.
#
# Return Value
#
# This method does not return any value.
# Example
# Open a file in write mode
fo = open("foo.txt", "rw+")
print("Name of the file: ", fo.name)

# Assuming file has following 5 lines
# This is 1st line
# This is 2nd line
# This is 3rd line
# This is 4th line
# This is 5th line

str = "This is 6th line"
# Write a line at the end of the file.
fo.seek(0, 2)
line = fo.write(str)

# Now read complete file from beginning.
fo.seek(0, 0)
for index in range(6):
line = fo.next()
print("Line No %d - %s" % (index, line))

# Close opend file
fo.close()
