def gcd(a,b):
    gcd = 1
    t = a
    l = b
    while max(a,b) % min(a,b) != 0:
        temp = min(a,b)
        b = max(a,b) % min(a,b)
        a = temp
    return min(a,b)

def lcm(a,b):
    return a*b//gcd(a,b)

n = int(input())
tree = list()
dist = list()
temp = 0
for i in range(n):
    tree.append(int(input()))
    if i == 0:
        continue
    else:
        dist.append(tree[i]-tree[i-1])
        if i == 1:
            temp = dist[0]
            continue
        else:
            temp = gcd(temp, dist[i-1])
print(sum(dist)//temp-len(dist))