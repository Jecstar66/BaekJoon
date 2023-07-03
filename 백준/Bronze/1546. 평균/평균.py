## Use map(int, input().split()) for integer input allocation.
import math
import sys

n = int(input())
arr = list(map(int,input().split()))
max_score = max(arr)
avg = 0
for i in range(n):
    arr[i] = arr[i]/max_score*100
    avg += arr[i]/n
print(avg)