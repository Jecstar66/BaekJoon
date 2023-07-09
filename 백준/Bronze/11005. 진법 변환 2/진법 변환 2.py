x, b = map(int, input().split())
c = ""

while x != 0:
    if x%b <= 9:
        c = str(x%b) + c
    else:
        c = chr(x%b+55) + c
    x = x // b
print(c)