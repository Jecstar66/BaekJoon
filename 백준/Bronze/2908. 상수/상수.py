## Use map(int, input().split()) for integer input allocation.
## Reference : https://dev-mandos.tistory.com/124
import math
import sys

a, b = map(int,input().split())
a = a//100+(a-100*(a//100)-(a%10))+100*(a%10)
b = b//100+(b-100*(b//100)-(b%10))+100*(b%10)

print(max(a,b))