## Use map(int, input().split()) for integer input allocation.
## Reference : https://dev-mandos.tistory.com/124
import math
import sys

plate = [[0 for _ in range(100)] for _ in range(100)] 
n = int(input())
for i in range(n):
    x, y = map(int,input().split())
    for a in range(x,x+10):
        for b in range(y,y+10):
            plate[a][b] = 1
            
sum = 0
for i in range(100):
    for j in range(100):
        sum += plate[i][j]
print(sum)