## Use map(int, input().split()) for integer input allocation.
import math

arr = [-1 for i in range(40)] ## 0 1 1 2 3 5 8
arr[0] = 0
arr[1] = 1

def fibonacci(n):
    if (n == 0) :
        return 0
    elif (n == 1) :
        return 1
    else :
        if arr[n-1] == -1:
            arr[n-1] = fibonacci(n-1)
        if arr[n-2] == -1:
            arr[n-2] == fibonacci(n-2)
    
        return arr[n-1] + arr[n-2]
    
T = int(input())

for i in range(T):
    n = int(input())
    if n == 0 :
        print("1 0")
    elif n == 1 :
        print("0 1")
    else:
        print(str(fibonacci(n-1))+" "+str(fibonacci(n)))