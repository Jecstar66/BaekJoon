def chess(arr):
    count = 0
    if(arr[0][0]=="B"):
        for i in range(8):
            for j in range(8):
                if((i+j)%2==0):
                    if(arr[i][j]=="W"):
                        count = count + 1
                else:
                    if(arr[i][j]=="B"):
                        count = count + 1
    else:
        for i in range(8):
            for j in range(8):
                if((i+j)%2==0):
                    if(arr[i][j]=="B"):
                        count = count + 1
                else:
                    if(arr[i][j]=="W"):
                        count = count + 1
    if count > 32:
        count = 64 - count
    return count

N, M = input().split()
N = int(N) ## 행 개수
M = int(M) ## 열 개수
arr = [[""]*M for i in range(N)]
for i in range(N):
    arr[i] = list(input())

ans = N*M
for i in range(N-7):
    for j in range(M-7):

        temp = chess([row[j:j+8] for row in arr[i:i+8]])
        if ans > temp:
            ans = temp
print(ans) 