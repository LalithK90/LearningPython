str = "this is string example....wow!!!"

sub = "i"
print("str.count(sub, 4, 40) : ", str.count(sub, 4, 40))
sub = "wow"
print("str.count(sub) : ", str.count(sub))

# Description
#
# The method count() returns the number of occurrences of substring sub in the range [start, end]. Optional arguments
# start and end are interpreted as in slice notation. Syntax
#
# str.count(sub, start= 0,end=len(string))
#
# Parameters
#
# sub − This is the substring to be searched.
#
# start − Search starts from this index. First character starts from 0 index. By default search starts from 0 index.
#
# end − Search ends from this index. First character starts from 0 index. By default search ends at the last index.
