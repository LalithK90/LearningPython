import re

text = open("regex_sum_1258897.txt")

values = []

for value in re.findall('[0-9]+', text.read()):
    values.append(int(value))

print(sum(values))
