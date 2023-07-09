import sys
gcd = 1
a, b = map(int, input().split())
t = a
l = b
while max(a,b) % min(a,b) != 0:
    temp = min(a,b)
    b = max(a,b) % min(a,b)
    a = temp
    
gcd = min(a,b)
print(t*l//gcd)