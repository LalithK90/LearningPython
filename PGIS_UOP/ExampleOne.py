import math

# Taking the input from user
number: int = int(input("Enter the Number"))

root = math.sqrt(number)
if int(root) ** 2 == number:
    print(number, "is a perfect square")
else:
    print(number, "is not a perfect square")