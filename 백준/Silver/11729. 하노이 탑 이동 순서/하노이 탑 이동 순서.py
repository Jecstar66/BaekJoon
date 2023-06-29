N = int(input())
def hanoi(n, start, by, end):
    if n == 1:
        print(start, end)
        return
    else:
        hanoi(n-1, start, end, by)
        print(start, end)
        hanoi(n-1, by, start, end)
print(2**N-1)
hanoi(N, 1, 2, 3)