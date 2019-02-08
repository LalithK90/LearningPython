str = "this is string example....wow!!!"
print(str.ljust(50, '0'))
# Description
#
# The method ljust() returns the string left justified in a string of length width. Padding is done using the
# specified fillchar (default is a space). The original string is returned if width is less than len(s). Syntax
#
# Following is the syntax for ljust() method −
#
# str.ljust(width[, fillchar])
#
# Parameters
#
#     width − This is string length in total after padding.
#
#     fillchar − This is filler character, default is a space.
#
# Return Value
#
# This method returns the string left justified in a string of length width. Padding is done using the specified
# fillchar (default is a space). The original string is returned if width is less than len(s).