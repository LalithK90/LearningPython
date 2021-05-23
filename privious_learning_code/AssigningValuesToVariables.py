print("Assigning Values to Variables \n")
note1 = '''Python variables do not need explicit declaration to reserve memory space. 
The declaration happens automatically when you assign a value to a variable. 
The equal sign (=) is used to assign values to variables.
The operand to the left of the = operator is the name of the variable and the operand to the right of the = operator is the value stored in the variable.
'''
print(note1)


counter = 100          # An integer assignment
miles   = 1000.0       # A floating point
name    = "Lalith"       # A string

print(counter)
print(miles)
print(name+"\n")

print("Multiple Assignment \n")
# Python allows you to assign a single value to several variables simultaneously.
a = b = c = 10
print(a)
print(b)
print(c)
print(a+b+c)
# Here, an integer object is created with the value 1, and all three variables are assigned to the same memory location.
# You can also assign multiple objects to multiple variables.
a,b,c = "Lalith",1,2

print("\n"+a)
print(b)
print(c)

#             Numbers
print("\n Numbers")

# v = 0122L python version 3.6 not support long
x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))

#           String
print("\n String")


str = 'Hello Python!'

print(str)          # Prints complete string
print(str[0])       # Prints first character of the string
print(str[2:5])     # Prints characters starting from 3rd to 5th
print(str[2:])      # Prints string starting from 3rd character
print(str * 2)      # Prints string two times
print(str + "TEST") # Prints concatenated string

#           List
print("\n List")

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print(list)             # Prints complete list
print(list[0])          # Prints first element of the list
print(list[1:3])        # Prints elements starting from 2nd till 3rd
print(list[2:])         # Prints elements starting from 3rd element
print(tinylist * 2)     # Prints list two times
print(list + tinylist)  # Prints concatenated lists

#       Tuples
print("\n Tuples")
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print(tuple)               # Prints complete list
print(tuple[0])            # Prints first element of the list
print(tuple[1:3])          # Prints elements starting from 2nd till 3rd
print(tuple[2:])           # Prints elements starting from 3rd element
print(tinytuple * 2)       # Prints list two times
print(tuple + tinytuple)   # Prints concatenated lists

#           Dictionary
print("\n Dictionary")
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}


print(dict['one'])       # Prints value for 'one' key
print(dict[2])           # Prints value for 2 key
print(tinydict)          # Prints complete dictionary
print(tinydict.keys())   # Prints all the keys
print(tinydict.values()) # Prints all the values