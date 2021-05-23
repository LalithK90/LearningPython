str1 = "this is string example....wow!!!"
str2 = "exam"

print(str1.find(str2))
print(str1.find(str2, 10))
print(str1.find(str2, 40))

# Description
#
# It determines if string str occurs in string, or in a substring of string if starting index beg and ending index
# end are given. Syntax
#
# str.find(str, beg=0, end=len(string))
#
# Parameters
#
#     str − This specifies the string to be searched.
#
#     beg − This is the starting index, by default its 0.
#
#     end − This is the ending index, by default its equal to the length of the string.
#
# Return Value
#
# Index if found and -1 otherwise.
