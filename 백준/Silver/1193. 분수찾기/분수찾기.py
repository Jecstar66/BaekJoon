import sys
x = int(input())
i = 0
if x == 1:
    print("1/1")
    sys.exit()
while True:
    i += 1
    x -= i
    if x <= (i+1):
        i += 1
        break
if i % 2 == 1:
    print("%d/%d" % (i-x+1,x))
else:
    print("%d/%d" % (x,i-x+1))