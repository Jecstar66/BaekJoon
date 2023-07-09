import math
n = int(input())
gcd = 1
for _ in range(n):
    a,b = map(int,input().split())
    if a%b==0 or b%a==0:
        print(max(a,b))
        continue
    else:
        for i in range(min(a,b),0,-1):
           if a % i == 0 and b % i == 0:
               gcd = i
               break
          
    print(a*b//gcd)