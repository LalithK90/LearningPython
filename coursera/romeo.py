fh = open("romeo.txt")
lst = list()
for line in fh:
    for new_one in line.split():
        if new_one not in lst:
            lst.append(new_one)
            print(new_one)

lst.sort()
print(lst)
