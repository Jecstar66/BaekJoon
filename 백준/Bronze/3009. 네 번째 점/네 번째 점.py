x = list()
y = list()
for _ in range(3):
    a, b = map(int,input().split())
    x.append(a)
    y.append(b)
if x[0] == x[1]:
    m = x[2]
elif x[0] == x[2]:
    m = x[1]
else:
    m = x[0]
if y[0] == y[1]:
    n = y[2]
elif y[0] == y[2]:
    n = y[1]
else:
    n = y[0]

print("%d %d" % (m,n))