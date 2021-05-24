from string import maketrans   # Required to call maketrans function.

intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)

str = "this is string example....wow!!!"
print(str.translate(trantab))

# Following is the example to delete 'x' and 'm' characters from the string −
#
# from string import maketrans   # Required to call maketrans function.
#
# intab = "aeiou"
# outtab = "12345"
# trantab = maketrans(intab, outtab)
#
# str = "this is string example....wow!!!"
# print(str.translate(trantab, 'xm'))






# Description
#
# The method translate() returns a copy of the string in which all characters have been translated using table (constructed with the maketrans() function in the string module), optionally deleting all characters found in the string deletechars.
# Syntax
#
# Following is the syntax for translate() method −
#
# str.translate(table[, deletechars]);
#
# Parameters
#
# table − You can use the maketrans() helper function in the string module to create a translation table.
#
# deletechars − The list of characters to be removed from the source string.
#
# Return Value
#
# This method returns a translated copy of the string.