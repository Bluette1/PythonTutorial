m, n = input().split()

a = [[int(s) for s in input().split()] for i in range(int(m))]

i, j = input().split()

for k in range(int(m)):
    a[k][int(i)], a[k][int(j)] = a[k][int(j)], a[k][int(i)]

print(a)

