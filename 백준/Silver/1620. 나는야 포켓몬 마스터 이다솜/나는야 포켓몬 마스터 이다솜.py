## Coded in Laptop.
import sys
n, q = map(int,input().split())
no2pok = dict()
pok2no = dict()
for i in range(1,n+1):
    pokemon = sys.stdin.readline().rstrip()
    no2pok[i] = pokemon
pok2no = {v:k for k,v in no2pok.items()}

for _ in range(q):
    quiz = sys.stdin.readline().rstrip()
    if ord(quiz[0]) < 65:
        print(no2pok[int(quiz)])
    else:
        print(pok2no[quiz])