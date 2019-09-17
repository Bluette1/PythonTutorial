n = int(input())
a = [[0] * n for i in range(n)]

j = n
for i in range(n):
    j -= 1
    a[i][j] = 1

for k in range(1, n):
    j = n
    for i in range(k, n):
        j -= 1
        a[i][j] = 2

for i in range(n):
    print(a[i])


