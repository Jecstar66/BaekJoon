## Use map(int, input().split()) for integer input allocation.
## Commentation : Alt + Shift + A

n = int(input())
log = dict()
for _ in range(n):
    name, inout = input().split()
    log[name] = inout

name = list()
for (k,v) in log.items():
    if v == "enter":
        name.append(k)

name.sort(reverse=True)
for c in name:
    print(c)