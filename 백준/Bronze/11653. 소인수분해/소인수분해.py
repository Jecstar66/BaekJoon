N = int(input())
if N == 1:
    pass
else:
    tmp = 2
    while(N != 1):
        if N % tmp == 0:
            print(tmp)
            N = N // tmp
            tmp = 2
        else:
            tmp = tmp + 1