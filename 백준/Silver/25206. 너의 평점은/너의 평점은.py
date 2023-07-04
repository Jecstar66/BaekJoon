## Use map(int, input().split()) for integer input allocation.
## Reference : https://dev-mandos.tistory.com/124
import math
import sys

def grading(grad):
    if grad == "F":
        return 0
    if grad[1] == "+":
        return 69.5-ord(grad[0])
    else:
        return 69-ord(grad[0])
    
GPA = 0
count = 0
for i in range(20):
    subj, cred, grad = input().split()
    if grad == 'P':
        continue
    count += int(cred[0])
    GPA += int(cred[0]) * grading(grad)

print(GPA/count)