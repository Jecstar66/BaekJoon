## Use map(int, input().split()) for integer input allocation.
## Reference : https://dev-mandos.tistory.com/124
import math
import sys

n = int(input())
for _ in range(n):
    rep, w = input().split()
    rep = int(rep)
    out = ""
    for c in w:
        out += (c*rep)
    print(out)
    
        