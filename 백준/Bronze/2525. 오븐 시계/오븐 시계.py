## Use map(int, input().split()) for integer input allocation.
import math
h, m = map(int,input().split())
t = int(input())
th = t//60
tm = t-th*60
h += th
m += tm
if m >= 60:
    h += 1
    m -= 60
print(str(h%24)+" "+str(m))
