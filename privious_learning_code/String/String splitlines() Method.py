str = "Line1-a b c d e f\nLine2- a b c\n\nLine4- a b c d"
print(str.splitlines())
print(str.splitlines(0))
print(str.splitlines(3))
print(str.splitlines(4))
print(str.splitlines(5))
# Description
#
# The method splitlines() returns a list with all the lines in string, optionally including the line breaks (if num
# is supplied and is true) Syntax
#
# Following is the syntax for splitlines() method −
#
# str.splitlines( num=string.count('\n'))
#
# Parameters
#
# num − This is any number, if present then it would be assumed that line breaks need to be included in the lines.
#
# Return Value
#
# This method returns true if found matching string otherwise false.
