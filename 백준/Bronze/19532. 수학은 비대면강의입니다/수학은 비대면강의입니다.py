## Use map(int, input().split()) for integer input allocation.
import math
import sys

# Using Inverse Matrix -> O(1)
a,b,c,d,e,f = map(int,input().split())
x = (e*c-b*f)//(a*e-b*d)
y = (a*f-d*c)//(a*e-b*d)
print(str(x)+" "+str(y))