def blackjack(card, N, M):
    score = 0
    tmp = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if i==j or j==k or i==k:
                    continue
                else :
                    tmp = card[i] + card[j] + card[k]
                    if tmp > score and tmp <= M :
                        score = tmp
    
    return score         
    
    
N, M = input().split()
N = int(N)
M = int(M)
card = list(input().split())

for p in range(len(card)):
    card[p] = int(card[p])    

print(blackjack(card, N, M))