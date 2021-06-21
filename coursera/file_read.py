fh = open("mbox.short.txt")
all_values = 0.0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        count += 1
        line_one = float(line.split(':')[1].rstrip())
        all_values += float(line_one)

ave = all_values / count
print('Average spam confidence: ' + str(ave))
