print("Multi-Line Statements")
item_one = 2
item_two = 4
item_three = 6

total = item_one + \
        item_two + \
        item_three

# Statements in Python typically end with a new line.
# Python does, however, allow the use of the line continuation character (\) to denote that the line should continue.
print(total)

# Statements contained within the [], {}, or () brackets do not need to use the line continuation character
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']

print(days)