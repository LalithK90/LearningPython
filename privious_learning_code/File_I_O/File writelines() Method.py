# Description
#
# The method writelines() writes a sequence of strings to the file. The sequence can be any iterable object producing
# strings, typically a list of strings. There is no return value. Syntax
#
# Following is the syntax for writelines() method −
#
# fileObject.writelines( sequence )
#
# Parameters
#
# sequence − This is the Sequence of the strings.
#
# Return Value
#
# This method does not return any value.
# Example
# Open a file in witre mode
fo = open("foo.txt", "rw+")
print("Name of the file: ", fo.name)

# Assuming file has following 5 lines
# This is 1st line
# This is 2nd line
# This is 3rd line
# This is 4th line
# This is 5th line

seq = ["This is 6th line\n", "This is 7th line"]
# Write sequence of lines at the end of the file.
fo.seek(0, 2)
line = fo.writelines(seq)

# Now read complete file from beginning.
fo.seek(0, 0)
for index in range(7):
line = fo.next()
print("Line No %d - %s" % (index, line))

# Close opend file
fo.close()
