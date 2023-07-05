## Use map(int, input().split()) for integer input allocation.
## Reference : https://dev-mandos.tistory.com/124
import math
import sys

arr = [[-1 for _ in range(15)] for _ in range(5)] 

for i in range(5):
    src = input()
    arr[i] = [c for c in src] + [-1 for i in range(15-len(src))]

for j in range(15):
    for i in range(5):
        if arr[i][j] != -1:
            print(arr[i][j], end="")
            