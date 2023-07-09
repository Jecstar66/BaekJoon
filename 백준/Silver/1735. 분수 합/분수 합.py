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

a, b = map(int, input().split())
c, d = map(int, input().split())
nom = a*d + c*b
denom = b*d

print("%d %d" % (nom//gcd(nom,denom),denom//gcd(nom,denom)))