## Use map(int, input().split()) for integer input allocation.
## Reference : https://dev-mandos.tistory.com/124
import math
import sys

n, m = map(int,input().split())
arr1 = [[0 for _ in range(m)] for _ in range(n)] 
arr2 = [[0 for _ in range(m)] for _ in range(n)] 
for i in range(n):
    arr1[i] = list(map(int, input().split()))
for i in range(n):
    arr2[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(m):
        arr1[i][j] += arr2[i][j]
        print(arr1[i][j], end = " ")
    print("")