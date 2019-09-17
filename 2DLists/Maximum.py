m, n = input().split()

a = [[int(s) for s in input().split()] for i in range(int(m))]
max = 0
imax, jmax = 0, 0
for i in range(int(m)):
    for j in range(int(n)):
        if a[i][j] > max:
            max = a[i][j]
            imax, jmax = i, j

print(imax, jmax)