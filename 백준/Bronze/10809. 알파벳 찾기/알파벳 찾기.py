## Use map(int, input().split()) for integer input allocation.
## Reference : https://dev-mandos.tistory.com/124
import math
import sys

S = input()
arr = [-1 for _ in range(26)]
count = 0
for w in S:
    if arr[ord(w)-97] != -1:
        count += 1
        continue
    arr[ord(w)-97] = count
    count += 1

for i in arr:
    print(i, end=" ")