print(" Python - Tuples\n")
print("\nAccessing Values in Tuples\n")
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)
print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])
print("\nUpdating Tuples\n")

tup3 = (12, 34.56)
tup4 = ('abc', 'xyz')

# Following action is not valid for tuples
# tup1[0] = 100;

# So let's create a new tuple as follows
tup5 = tup3 + tup4
print(tup5)
print("\nDelete Tuple Elements\n")
tup = ('physics', 'chemistry', 1997, 2000)
print(tup)
print("remove comment see the delete function")
# del tup
# print("After deleting tup : ")
# print(tup)
print("\nNo Enclosing Delimiters\n")
print('abc', -4.24e93, 18 + 6.6j, 'xyz')
x, y = 1, 2
print("Value of x , y : ", x, y)

print("\nCompares elements of both tuples.\n")
print("\nGives the total length of the tuple.\n")
print("\nReturns item from the tuple with max value.\n")
print("\nReturns item from the tuple with min value.\n")
print("\nConverts a list into tuple.\n")
