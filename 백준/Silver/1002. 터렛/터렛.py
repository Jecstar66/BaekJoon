## Use map(int, input().split()) for integer input allocation.

import math
T = int(input())
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = (x1-x2)**2+(y1-y2)**2  
    if (x1, y1, r1) == (x2, y2, r2) :
        print(-1)
        continue
    elif (x1, y1) == (x2, y2) and r1 != r2 :
        print(0)
        continue
    elif dist == (r1+r2)**2 or dist == (r2-r1)**2:
        print(1)
        continue
    elif dist > (r1+r2)**2 or dist < (r2-r1)**2:
        print(0)
        continue
    else:
        print(2)