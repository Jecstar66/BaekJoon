## Use map(int, input().split()) for integer input allocation.
## Reference : https://dev-mandos.tistory.com/124
import math
import sys

n = int(input())
count = 0
for i in range(n):
    w = input()
    arr = [0 for _ in range(26)]
    flag = 1
    for i in range(len(w)):
        if i == 0:
            arr[ord(w[i])-97] = 1
            continue
        
        if arr[ord(w[i])-97] == 0 and w[i] != w[i-1]:
            arr[ord(w[i])-97] = 1
        
        elif arr[ord(w[i])-97] != 0 and w[i] == w[i-1]:
            continue
        
        elif arr[ord(w[i])-97] != 0 and w[i] != w[i-1]:
            flag = 0
            break
    if flag == 1:
        count += 1
        
print(count)
        
        
        