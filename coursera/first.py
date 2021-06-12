largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        numbers = int(num)
    except:
        print('Invalid input')
        continue
    if smallest is None:
        smallest = numbers
    if smallest > numbers:
        smallest = numbers
    if largest is None:
        largest = numbers
    if numbers > largest:
        largest = numbers

print("Maximum is", largest)
print("Minimum is", smallest)
