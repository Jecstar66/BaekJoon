def creator(N):
    tmp = N
    sum = N
    while(tmp!=0):
        sum = sum + tmp % 10
        tmp = tmp // 10
    return sum

N = int(input())
for i in range(N):
    tmp = creator(i)
    if tmp == N:
        print(i)
        break
    if i == (N-1):
        print(0)
        break
    

        