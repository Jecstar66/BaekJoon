## Use map(int, input().split()) for integer input allocation.
## Reference : https://dev-mandos.tistory.com/124
import math
import sys

n = int(input())
ans = input()
sum = 0
for i in ans:
    sum += int(i)
print(sum)