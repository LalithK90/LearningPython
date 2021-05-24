
# Description
#
# The method get() returns a value for the given key. If key is not available then returns default value None.
# Syntax
#
# Following is the syntax for get() method −
#
# dict.get(key, default = None)
#
# Parameters
#
# key − This is the Key to be searched in the dictionary.
#
# default − This is the Value to be returned in case key does not exist.
#
# Return Value
#
# This method return a value for the given key. If key is not available, then returns default value None.
# Example
dict = {'Name': 'Zabra', 'Age': 7}
print("Value : %s" %  dict.get('Age'))
print("Value : %s" %  dict.get('Education', "Never"))