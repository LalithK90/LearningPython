print("\n LOOP\n")

print("\n while loop \n")
count = 0
while count < 9:
print('The count is:', count)
count = count + 1

print("Good bye!\n")
print(" The Infinite Loop (if you want to see this please remove comment following )")
# var = 1
# while var == 1:  # This constructs an infinite loop
# num = input("Enter a number  :")
# print("You entered: ", num)
#
# print("Good bye!\n")
print(" Using else Statement with Loops (if you want to see this please remove comment following )")
# count = 0
# while count < 5:
# print(count, " is  less than 5")
# count = count + 1
# else:
# print(count, " is not less than 5\n")
#
# flag = 1
# while flag: print('Given flag is really true!')
# print("Good bye!\n")

print("\n   for loop \n")
for letter in 'Python':  # First Example
print('Current Letter :', letter)

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:  # Second Example
print('Current fruit :', fruit)

print("Good bye!")

print("\n Iterating by Sequence Index\n")
fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
print('Current fruit :', fruits[index])

print("\nGood bye!\n")

print("\n Using else Statement with Loops \n")

for num in range(10, 20):  # to iterate between 10 to 20
for i in range(2, num):  # to iterate on the factors of the number
if num % i == 0:  # to determine the first factor
j = num / i  # to calculate the second factor
print('%d equals %d * %d' % (num, i, j))
break  # to move to the next number, the #first FOR
else:  # else part of the loop
print(num, 'is a prime number')

print("\n nested loops \n")
i = 2
while i < 100:
j = 2
while j <= (i / j):
if not (i % j): break
j = j + 1
if j > i / j: print(i, " is prime")
i = i + 1

print("Good bye!\n")

print(" Loop Control Statements ")
print("\n break statement \n")
for letter in 'Python':  # First Example
if letter == 'h':
break
print('Current Letter :', letter)

var = 10  # Second Example
while var > 0:
print('Current variable value :', var)
var = var - 1
if var == 5:
break

print("Good bye!")

print("\n continue statement \n")
for letter in 'Python':  # First Example
if letter == 'h':
continue
print('Current Letter :', letter)

var = 10  # Second Example
while var > 0:
var = var - 1
if var == 5:
continue
print('Current variable value :', var)
print("Good bye!")

print("\n pass Statement \n")
for letter in 'Python':
if letter == 'h':
pass
print('This is pass block')
print('Current Letter :', letter)
print("Good bye!")
