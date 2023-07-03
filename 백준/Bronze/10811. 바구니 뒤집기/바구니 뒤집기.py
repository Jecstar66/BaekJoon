## Use map(int, input().split()) for integer input allocation.
import math
import sys

n, m = map(int, input().split())
arr = [i+1 for i in range(n)]
for _ in range(m):
    low, high = map(int, input().split())
    for i in range((high-low)//2+1):
        temp = arr[low-1+i]
        arr[low-1+i] = arr[high-1-i]
        arr[high-1-i] = temp
for i in range(len(arr)):
    print(arr[i], end=" ")
    