str1 = "this is string example....wow!!!"
str2 = "is"

print(str1.rindex(str2))
print(str1.index(str2))

# Description
#
# The method rindex() returns the last index where the substring str is found, or raises an exception if no such index exists, optionally restricting the search to string[beg:end].
# Syntax
#
# Following is the syntax for rindex() method −
#
# str.rindex(str, beg=0 end=len(string))
#
# Parameters
#
# str − This specifies the string to be searched.
#
# beg − This is the starting index, by default its 0
#
# len − This is ending index, by default its equal to the length of the string.
#
# Return Value
#
# This method returns last index if found otherwise raises an exception if str is not found.