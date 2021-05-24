
# Description
#
# The method list() takes sequence types and converts them to lists. This is used to convert a given tuple into list.
#
# Note − Tuple are very similar to lists with only difference that element values of a tuple can not be changed and tuple elements are put between parentheses instead of square bracket.
# Syntax
#
# Following is the syntax for list() method −
#
# list( seq )
#
# Parameters
#
# seq − This is a tuple to be converted into list.
#
# Return Value
#
# This method returns the list.
# Example
aTuple = (123, 'xyz', 'zara', 'abc')
aList = list(aTuple)
print("List elements : ", aList)