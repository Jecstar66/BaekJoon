count = 1
index = 1
temp = 0

for i in range(9):
    a = int(input())
    if a > temp:
        temp = a
        index = count
    count += 1

print(temp)
print(index)