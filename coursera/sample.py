x = (5, 1, 3)
y = (6, 5, 0)
if y > x:
    print(y)

c = {'chuck': 1, 'fred': 42, 'jan': 100}
tmp = list()
for k, v in c.items():
    tmp.append((v, k))
print(tmp)
print(type(c.items()))

days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print(days[2])