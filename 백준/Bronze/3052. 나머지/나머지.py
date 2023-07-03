## Use map(int, input().split()) for integer input allocation.
import math
import sys

arr = []
for i in range(10):
    temp = int(input())%42
    if temp not in arr:
        arr.append(temp)
print(len(arr)) 