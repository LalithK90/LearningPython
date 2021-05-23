str = "this is string example....wow!!!"
print(str.startswith('this'))
print(str.startswith('is', 2, 4))
print(str.startswith('this', 2, 4))
# Description
#
# The method startswith() checks whether string starts with str, optionally restricting the matching with the given
# indices start and end. Syntax
#
# Following is the syntax for startswith() method −
#
# str.startswith(str, beg=0,end=len(string));
#
# Parameters
#
#     str − This is the string to be checked.
#
#     beg − This is the optional parameter to set start index of the matching boundary.
#
#     end − This is the optional parameter to end start index of the matching boundary.
#
# Return Value
#
# This method returns true if found matching string otherwise false.
