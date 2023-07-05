## Use map(int, input().split()) for integer input allocation.
## Reference : https://dev-mandos.tistory.com/124
import math
import sys

w = input()
arr = [0 for _ in range(26)]
for c in w:
    if ord(c) >= 97:
        arr[ord(c)-97] += 1
    else:
        arr[ord(c)-65] += 1
        
temp = 0
for i in range(len(arr)):
    if arr[i] == max(arr) and temp == 0:
        temp = chr(65+i)
    elif arr[i] == max(arr) and temp != 0:
        print("?")
        sys.exit()
    else:
        continue
print(temp)