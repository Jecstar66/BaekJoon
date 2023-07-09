w, b = input().split()
num = 0
power = len(w)-1
for c in w:
    if ord(c) < 65:
        num += int(c)*pow(int(b),power)
    else:
        num += (ord(c)-55)*pow(int(b),power)
    power -= 1
print(num)
        