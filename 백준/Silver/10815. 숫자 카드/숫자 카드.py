## Use map(int, input().split()) for integer input allocation.
## Commentation : Alt + Shift + A

import math

n = int(input())
card = set(map(int,input().split()))
m = int(input())
sang = list(map(int,input().split()))

for c in sang:
    if c in card:
        print(1,end=" ")
    else:
        print(0,end=" ")
        