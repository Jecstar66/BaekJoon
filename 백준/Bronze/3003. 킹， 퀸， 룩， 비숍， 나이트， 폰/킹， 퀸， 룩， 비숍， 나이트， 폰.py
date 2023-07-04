## Use map(int, input().split()) for integer input allocation.
## Reference : https://dev-mandos.tistory.com/124
import math
import sys

arr = list(map(int,input().split()))
ans = [1,1,2,2,2,8]
for i in range(len(arr)):
    print(ans[i]-arr[i], end=" ")