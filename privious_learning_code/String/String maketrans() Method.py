from string import maketrans  # Required to call maketrans function.

intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)

str = "this is string example....wow!!!"
print(str.translate(trantab))
# Description
#
# The method maketrans() returns a translation table that maps each character in the intabstring into the character
# at the same position in the outtab string. Then this table is passed to the translate() function.
#
# Note − Both intab and outtab must have the same length.
# Syntax
#
# Following is the syntax for maketrans() method −
#
# str.maketrans(intab, outtab)
#
# Parameters
#
# intab − This is the string having actual characters.
#
# outtab − This is the string having corresponding mapping character.
#
# Return Value
#
# This method returns a translate table to be used translate() function.
