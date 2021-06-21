fh = open("mbox.short.txt")
count = 0
for line in fh:
    if line.startswith("From:"):
        count += 1
        print(line.split("From:")[1].rstrip())

print("There were", count, "lines in the file with From as the first word")
