N = int(input())
arr = list(map(int, input().split()))
count = 0
for i in range(len(arr)):
    tmp = arr[i]
    if tmp == 1:
        continue
    flag = True
    for j in range(2, tmp):
        if tmp % j == 0:
            flag = False
    if flag == True:
        count = count + 1
print(count)