## Use map(int, input().split()) for integer input allocation.
## Reference : https://dev-mandos.tistory.com/124
import math
import sys

n = int(input())
for i in range(2*n-1):
    print(" "*abs(n-1-i)+"*"*min(2*i+1,4*n-3-2*i))