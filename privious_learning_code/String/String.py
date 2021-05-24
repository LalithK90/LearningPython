print("\n   Python - Strings\n")

print("\n Accessing Values in Strings\n")
var1 = 'Hello World!'
var2 = "Python Programming"

print("var1[0]: ", var1[0])
print("var2[1:5]: ", var2[1:5])

print("\nUpdating Strings\n")
var1 = 'Hello World!'
print("Updated String :- ", var1[:6] + 'Python')
print("\nString Formatting Operator\n")
print("My name is %s and weight is %d kg!" % ('Zara', 21))

print("\nTriple Quotes\n")
para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print(para_str)

print('C:\\nowhere')

print(r'C:\\nowhere')

print("\nUnicode String\n")
print(u'Hello, world!')

print("\nCapitalizes first letter of string\n")
print("\nReturns a space-padded string with the original string centered to a total of width columns.\n")
print("\nCounts how many times str occurs in string or in a substring of string if starting index beg and ending index end are given.\n")
print("\nDecodes the string using the codec registered for encoding. encoding defaults to the default string encoding.\n")
print("\nReturns encoded string version of string; on error, default is to raise a ValueError unless errors is given with 'ignore' or 'replace'.\n")
print("\nDetermines if string or a substring of string (if starting index beg and ending index end are given) ends with suffix; returns true if so and false otherwise.\n")
print("\nExpands tabs in string to multiple spaces; defaults to 8 spaces per tab if tabsize not provided.\n")
print("\nDetermine if str occurs in string or in a substring of string if starting index beg and ending index end are given returns index if found and -1 otherwise.\n")
print("\nSame as find(), but raises an exception if str not found.\n")
print("\nReturns true if string has at least 1 character and all characters are alphanumeric and false otherwise.\n")
print("\nReturns true if string has at least 1 character and all characters are alphabetic and false otherwise.\n")
print("\nReturns true if string contains only digits and false otherwise.\n")
print("\nReturns true if string has at least 1 cased character and all cased characters are in lowercase and false otherwise.\n")
print("\nReturns true if a unicode string contains only numeric characters and false otherwise.\n")
print("\nReturns true if string contains only whitespace characters and false otherwise.\n")
print("\nReturns true if string is properly \"titlecased\" and false otherwise.\n")
print("\nReturns true if string has at least one cased character and all cased characters are in uppercase and false otherwise.\n")
print("\nMerges (concatenates) the string representations of elements in sequence seq into a string, with separator string.\n")
print("\nReturns the length of the string\n")
print("\nReturns a space-padded string with the original string left-justified to a total of width columns.\n")
print("\nConverts all uppercase letters in string to lowercase.\n")
print("\nRemoves all leading whitespace in string.\n")
print("\nReturns a translation table to be used in translate function.\n")
print("\nReturns the max alphabetical character from the string str.\n")
print("\nReturns the min alphabetical character from the string str.\n")
print("\nReplaces all occurrences of old in string with new or at most max occurrences if max given.\n")
print("\nSame as find(), but search backwards in string.\n")
print("\nSame as index(), but search backwards in string.\n")
print("\nReturns a space-padded string with the original string right-justified to a total of width columns.\n")
print("\nRemoves all trailing whitespace of string.\n")
print("\nSplits string according to delimiter str (space if not provided) and returns list of substrings; split into at most num substrings if given.\n")
print("\nSplits string at all (or num) NEWLINEs and returns a list of each line with NEWLINEs removed.\n")
print("\nDetermines if string or a substring of string (if starting index beg and ending index end are given) starts with substring str; returns true if so and false otherwise.\n")
print("\nPerforms both lstrip() and rstrip() on string.\n")
print("\nInverts case for all letters in string.\n")
print("\nReturns \"titlecased\" version of string, that is, all words begin with uppercase and the rest are lowercase.\n")
print("\nTranslates string according to translation table str(256 chars), removing those in the del string.\n")
print("\nConverts lowercase letters in string to uppercase.\n")
print("\nReturns original string leftpadded with zeros to a total of width characters; intended for numbers, zfill() retains any sign given (less one zero).\n")
print("\nReturns true if a unicode string contains only decimal characters and false otherwise.\n")
