## Use map(int, input().split()) for integer input allocation.
## Reference : https://dev-mandos.tistory.com/124
import math
import sys

n = int(input())
for _ in range(n):
    S = input()
    print(S[0]+S[len(S)-1])