## Use map(int, input().split()) for integer input allocation.
## Commentation : Alt + Shift + A
## Advantage for Sieve Alg. : when [a range of number] is input
import math

T = int(input())
input_arr = list()
for _ in range(T):
    input_arr.append(int(input()))
max_input = max(input_arr)

""" arr = [i for i in range(2,max_input)]
pivot = 0
while pivot != len(arr):
    for num in arr:
        if num == arr[pivot]:
            continue
            
        if num % arr[pivot] == 0:
            arr.remove(num)
            
    pivot += 1
 """
lst = [True] * 1000000      #N: 1,000,000이하의 자연수 (어짜피 1,000,000은 소수 x)
lst[0] =lst[1] = False      #0,1은 소수X
for i in range(1000000):    #체 적용하기
    if lst[i]:
        for j in range(2*i,1000000,i):
            lst[j] = False
        
for i in range(T):
    count = 0
    x = input_arr[i]
    for j in range(1,int((x/2)+1)):
        if lst[j] and lst[x-j] :
            count += 1
    print(count)