n = int(input())
arr = list(map(int,input().split()))
find = int(input())
count = 0
for num in arr:
    if num == find:
        count += 1
print(count)