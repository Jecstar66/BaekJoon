## Use map(int, input().split()) for integer input allocation.
## Reference : https://dev-mandos.tistory.com/124
import math
import sys

while True:
    n = int(input())
    if n == -1:
        break
    
    arr = list()
    for i in range(1,n):
        if n % i == 0:
            arr.append(i)
    if sum(arr) == n:
        print("%d = 1 " % n, end = "")
        for c in arr:
            if c == 1:
                continue
            print("+ %d" % c, end = " ")
        print("")
    else: 
        print("%d is NOT perfect." % n)
