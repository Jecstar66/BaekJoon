import math
n = int(input())
for _ in range(n):
    x = int(input())
    if x <= 2:
        print(2)
        continue
        
    flag = 0
    while True:
        for i in range(2,math.floor(math.sqrt(x))+1):
            if x % i == 0:
                flag = 1
                break
        if flag == 1:
            flag = 0
            x += 1
            continue
        else:
            break
    print(x)