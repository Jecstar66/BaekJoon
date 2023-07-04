## Use map(int, input().split()) for integer input allocation.
## Reference : https://dev-mandos.tistory.com/124
import math
import sys

w = list(input())
hypen = w.count('-')
equal = 0
j = 0

for i in range(len(w)):
    if w[i] == '=':
        if w[i-2] == 'd' and w[i-1] == 'z':
            equal += 2
        else:
            equal += 1
    elif w[i] == 'j':
        if w[i-1] in ('l','n'):
            j += 1
print(len(w)-hypen-equal-j)
