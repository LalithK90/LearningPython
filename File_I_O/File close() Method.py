
# Description
#
# The method close() closes the opened file. A closed file cannot be read or written any more. Any operation, which requires that the file be opened will raise a ValueError after the file has been closed. Calling close() more than once is allowed.
#
# Python automatically closes a file when the reference object of a file is reassigned to another file. It is a good practice to use the close() method to close a file.
# Syntax
#
# Following is the syntax for close() method −
#
# fileObject.close();
#
# Parameters
#
#     NA
#
# Return Value
#
# This method does not return any value.
# Example
# Open a file
fo = open("foo.txt", "wb")
print("Name of the file: ", fo.name)

# Close opend file
fo.close()