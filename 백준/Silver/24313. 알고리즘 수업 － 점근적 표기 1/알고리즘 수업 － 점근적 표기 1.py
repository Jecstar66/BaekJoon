## Use map(int, input().split()) for integer input allocation.
## Reference : https://dev-mandos.tistory.com/124
import math
import sys

a1,a0 = map(int,input().split())
c = int(input())
n0 = int(input())
if c > a1:
    if n0 >= a0/(c-a1):
        print(1)
    else:
        print(0)
elif c == a1:
    if a0 <= 0:
        print(1)
    else:
        print(0)
else:
    print(0)