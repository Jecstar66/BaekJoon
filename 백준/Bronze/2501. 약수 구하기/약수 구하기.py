## Use map(int, input().split()) for integer input allocation.
## Reference : https://dev-mandos.tistory.com/124
import math
import sys

n, k = map(int,input().split())
arr = list()
for i in range(1,n+1):
    if n % i == 0:
        arr.append(i)

if len(arr) < k:
    print(0)
else:
    print(arr[k-1])