n = int(input())

a = [[0] * n for i in range(n)]
zero = 0  # set the position of 0

for i in range(n):
    # from zero position, traverse forwards filling in corresponding values (1, 2, 3...)
    for j in range(zero + 1, n):
        a[i][j] = j - i

    # from zero position, traverse backwards filling in corresponding values (1, 2, 3...)
    for j in range(zero - 1, -1, -1):
        a[i][j] = i - j
    zero += 1

for i in range(n):
    print(a[i])


