## Use map(int, input().split()) for integer input allocation.
## Reference : https://dev-mandos.tistory.com/124
import math
import sys

w = input()
for i in range(len(w)):
    if w[i] != w[len(w)-1-i]:
        print(0)
        sys.exit()
print(1)