## Use map(int, input().split()) for integer input allocation.
import math

n, m = map(int,input().split())
arr = [i+1 for i in range(n)]
for _ in range(m):
    g, t = map(int,input().split())
    temp = arr[g-1]
    arr[g-1] = arr[t-1]
    arr[t-1] = temp

for i in range(n):
    print(arr[i],end=" ") 