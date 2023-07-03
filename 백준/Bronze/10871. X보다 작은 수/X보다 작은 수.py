n, x = map(int,input().split())
arr = list(map(int,input().split()))
ans = ""
for num in arr:
    if num < x:
        ans += (str(num)+" ")
print(ans.rstrip())