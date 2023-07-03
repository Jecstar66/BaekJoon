## Use map(int, input().split()) for integer input allocation.
import math
import sys

bag = -1
n = int(input())
for i in range(n//5,-1,-1):
    if (n-5*i) % 3 == 0:
        bag = i + (n-5*i)//3
        break
print(bag)