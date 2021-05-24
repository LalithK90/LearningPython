str = "This Is String Example...Wow!!!"
print(str.istitle())

str = "This is string example....wow!!!"
print(str.istitle())
# Description
#
# The method istitle() checks whether all the case-based characters in the string following non-casebased letters are
# uppercase and all other case-based characters are lowercase. Syntax
#
# Following is the syntax for istitle() method −
#
# str.istitle()
#
# Parameters
#
# NA
#
# Return Value
#
# This method returns true if the string is a titlecased string and there is at least one character, for example
# uppercase characters may only follow uncased characters and lowercase characters only cased ones.It returns false
# otherwise.