print("                         Python - Dictionary\n")
print("\nAccessing Values in Dictionary\n")
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])
print("\nUpdating Dictionary\n")
dict1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict1['Age'] = 8; # update existing entry
dict1['School'] = "DPS School"; # Add new entry

print("dict1['Age']: ", dict1['Age'])

print("dict1['School']: ", dict1['School'])

print("\nDelete Dictionary Elements\n")
dict2 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
del dict2['Name']; # remove entry with key 'Name'
dict2.clear();     # remove all entries in dict
del dict2 ;        # delete entire dictionary

print("dict2['Age']: ", dict2['Age'])
print("dict2['School']: ", dict2['School'])

print("\nProperties of Dictionary Keys\n")
dict3 = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
print("dict3['Name']: ", dict3['Name'])
dict3 = {['Name']: 'Zara', 'Age': 7}
print("dict3['Name']: ", dict3['Name'])

print("\nBuilt-in Dictionary Functions & Methods\n")

print("\nCompares elements of both dict.\n")
print("\nGives the total length of the dictionary. This would be equal to the number of items in the dictionary.\n")
print("\nProduces a printable string representation of a dictionary\n")
print("\nReturns the type of the passed variable. If passed variable is dictionary, then it would return a dictionary type.\n")

print("\nRemoves all elements of dictionary dict\n")
print("\nReturns a shallow copy of dictionary dict\n")
print("\nCreate a new dictionary with keys from seq and values set to value.\n")
print("\nFor key key, returns value or default if key not in dictionary\n")
print("\nReturns true if key in dictionary dict, false otherwise\n")
print("\nReturns a list of dict's (key, value) tuple pairs\n")
print("\nReturns list of dictionary dict's keys\n")
print("\nSimilar to get(), but will set dict[key]=default if key is not already in dict\n")
print("\nAdds dictionary dict2's key-values pairs to dict\n")
print("\nReturns list of dictionary dict's values\n")