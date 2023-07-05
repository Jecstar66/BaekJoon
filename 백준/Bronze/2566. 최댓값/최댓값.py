## Use map(int, input().split()) for integer input allocation.
## Reference : https://dev-mandos.tistory.com/124
import math
import sys

arr = [[0 for _ in range(9)] for _ in range(9)] 

temp = 0
row = 0
col = 0
for i in range(9):
    arr[i] = list(map(int, input().split()))
    for j in range(9):
        if arr[i][j] >= temp:
            temp = arr[i][j]
            row = i+1
            col = j+1
print(temp)
print(str(row)+" "+str(col))