# N = int(input())
# arr = list(map(int, input().split()))
# count = 0
# for i in range(len(arr)):
#     tmp = arr[i]
#     if tmp == 1:
#         continue
#     flag = True
#     for j in range(2, tmp):
#         if tmp % j == 0:
#             flag = False
#     if flag == True:
#         count = count + 1
# print(count)

M = int(input())
N = int(input())
sum = 0
ans = 10000
for i in range(M,N+1):
    if i == 1:
        continue
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
    if flag == True:
        sum = sum + i
        if ans > i :
            ans = i
if sum != 0:
    print(sum)
    print(ans)
else:
    print(-1)