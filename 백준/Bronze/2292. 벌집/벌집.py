n = (int(input())-1)/6
i = 0
while n > 0:
    i += 1
    n -= i
print(i+1)