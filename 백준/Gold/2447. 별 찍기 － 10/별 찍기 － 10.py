def add_star(n):
    if n == 1 :
        return ["*"]
    star = add_star(int(n/3))
    arr = []

    for x in star:
        arr.append(x*3)
    for x in star:
        arr.append(x+" "*int(n/3)+x)
    for x in star:
        arr.append(x*3)
    return arr

n = int(input())
arr = add_star(n)
for i in range(n):
    print(arr[i])