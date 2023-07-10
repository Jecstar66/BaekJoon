## Use map(int, input().split()) for integer input allocation.
## Commentation : Alt + Shift + A
import math
arr = list()
for i in range(2,2*123456):
    flag = 0
    for j in range(2,math.floor(math.sqrt(i))+1):
        if i % j == 0:
            flag = 1
            break
    if flag == 1:
        flag = 0
        continue
    else:
        arr.append(i)

while True:
    x = int(input())
    if x == 0:
        break
    if x <= 2:
        print(1)
        continue
    
    count = 0
    for num in arr:
        if num > x and num <= 2*x:
            count += 1
    print(count)
        
    ## O(N^1/2) Algorithm 
    """ for i in range(x+1,2*x):
        flag = 0
        for j in range(2,math.floor(math.sqrt(i))+1):
            if i % j == 0:
                flag = 1
                break
        if flag == 1:
            flag = 0
            continue
        else:
            count += 1 """
            
    ## O(NloglogN) Algorithm (Sieve): Too Slow
    """ arr = [i for i in range(2,2*x)]
    pivot = 0
    while pivot != len(arr):
        for num in arr:
            if num == arr[pivot]:
                continue
            
            if num % arr[pivot] == 0:
                arr.remove(num)
        pivot += 1
        
    for num in arr:
        if num > x:
            count += 1
    print(count) """
    