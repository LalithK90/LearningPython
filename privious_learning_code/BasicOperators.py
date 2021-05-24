print("Basic Operators")
print("   Arithmetic Operators Example")
a = 31
b = 10
c = 0

c = a + b
print("\n Line 1 - Value of c is ", c)

c = a - b
print("\n Line 2 - Value of c is ", c)

c = a * b
print("\n Line 3 - Value of c is ", c)

c = a / b
print("\n Line 4 - Value of c is ", c)

c = a % b
print("\n Line 5 - Value of c is ", c)

a = 2
b = 3
c = a ** b
print("\n Line 6 - Value of c is ", c)

a = 10
b = 5
c = a // b
print("\n Line 7 - Value of c is ", c)

print("\n   Comparison Operators ")
a = 21
b = 10
c = 0

# Normally we write condition between parenthesis but python 3 and above version we can leave it
if a == b:
print("Line 1 - a is equal to b")
else:
print("Line 1 - a is not equal to b")

if a != b:
print("Line 2 - a is not equal to b")
else:
print("Line 2 - a is equal to b")

# Following method not support python 3 or above
# if ( a <> b ):
#print("Line 3 - a is not equal to b")
# else:
#print("Line 3 - a is equal to b")

if a < b:
print("Line 4 - a is less than b")
else:
print("Line 4 - a is not less than b")

if a > b:
print("Line 5 - a is greater than b")
else:
print("Line 5 - a is not greater than b")

a = 5
b = 20
if a <= b:
print("Line 6 - a is either less than or equal to  b")
else:
print("Line 6 - a is neither less than nor equal to  b")

if b >= a:
print("Line 7 - b is either greater than  or equal to b")
else:
print("Line 7 - b is neither greater than  nor equal to b")

print("\n Assignment Operators")
a = 21
b = 10
c = 0

c = a + b
print("Line 1 - Value of c is ", c)

c += a
print("Line 2 - Value of c is ", c)

c *= a
print("Line 3 - Value of c is ", c)

c /= a
print("Line 4 - Value of c is ", c)

c = 2
c %= a
print("Line 5 - Value of c is ", c)

c **= a
print("Line 6 - Value of c is ", c)

c //= a
print("Line 7 - Value of c is ", c)

print("\n   Bitwise Operators")
a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
c = 0

c = a & b;  # 12 = 0000 1100
print("Line 1 - Value of c is ", c)

c = a | b;  # 61 = 0011 1101
print("Line 2 - Value of c is ", c)

c = a ^ b;  # 49 = 0011 0001
print("Line 3 - Value of c is ", c)

c = ~a;  # -61 = 1100 0011
print("Line 4 - Value of c is ", c)

c = a << 2;  # 240 = 1111 0000
print("Line 5 - Value of c is ", c)

c = a >> 2;  # 15 = 0000 1111
print("Line 6 - Value of c is ", c)

print("\n   Logical Operators   ")

a = True
b = False
c = True
x = False
# y = True
# z = False

# And = If both the operands are true then condition becomes true.
print("Example 1")
if a and b:
print("a and b is  same boolean value")
else:
print("a and b is not a same boolean value")
print("Example 2")
if a and c:
print("a and c is  same boolean value")
else:
print("a and c is not a same boolean value")

# OR = If any of the two operands are non-zero then condition becomes true.
print("Example - 1")
if a or b:
print("a or b is  true in boolean value")
print("Example - 2")
if a or x:
print("a or x is not true in boolean value")
# Not = Used to reverse the logical state of its operand.
if not (a and b):
print("a and b is not a same boolean value")
else:
print("a and b is same boolean value")

print("\n   Membership Operators")
a = 10
b = 20
listSample = [1, 2, 3, 4, 5];

if a in listSample:
print("Line 1 - a is available in the given list")
else:
print("Line 1 - a is not available in the given list")

if b not in listSample:
print("Line 2 - b is not available in the given list")
else:
print("Line 2 - b is available in the given list")

a = 2
if a in listSample:
print("Line 3 - a is available in the given list")
else:
print("Line 3 - a is not available in the given list")

print("\n   Identity Operators")

a = 20
b = 20

if a is b:
print("Line 1 - a and b have same identity")
else:
print("Line 1 - a and b do not have same identity")

if id(a) == id(b):
print("Line 2 - a and b have same identity")
else:
print("Line 2 - a and b do not have same identity")

b = 30
if a is b:
print("Line 3 - a and b have same identity")
else:
print("Line 3 - a and b do not have same identity")

if a is not b:
print("Line 4 - a and b do not have same identity")
else:
print("Line 4 - a and b have same identity")

print("\n   Operators Precedence")

a = 20
b = 10
c = 15
d = 5
e = 0

e = (a + b) * c / d  # ( 30 * 15 ) / 5
print("Value of (a + b) * c / d is ", e)

e = ((a + b) * c) / d  # (30 * 15 ) / 5
print("Value of ((a + b) * c) / d is ", e)

e = (a + b) * (c / d)  # (30) * (15/5)
print("Value of (a + b) * (c / d) is ", e)

e = a + (b * c) / d  # 20 + (150/5)
print("Value of a + (b * c) / d is ", e)
