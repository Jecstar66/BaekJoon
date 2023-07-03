## Use map(int, input().split()) for integer input allocation.
import math

n, m = map(int,input().split())
arr = [0 for i in range(n)]
for i in range(m):
    low, high, ball = map(int,input().split())
    for ind in range(low-1,high):
        arr[ind] = ball

ans = ""
for i in arr:
    ans += (str(i)+" ")
print(ans)