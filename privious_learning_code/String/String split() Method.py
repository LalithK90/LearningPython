str = "Line1-abcdef \nLine2-abc \nLine4-abcd"
print(str.split())
print(str.split(' ', 1))
# Description
#
# The method split() returns a list of all the words in the string, using str as the separator (splits on all
# whitespace if left unspecified), optionally limiting the number of splits to num. Syntax
#
# Following is the syntax for split() method −
#
# str.split(str="", num=string.count(str)).
#
# Parameters
#
# str − This is any delimeter, by default it is space.
#
# num − this is number of lines minus one
#
# Return Value
#
# This method returns a list of lines.
