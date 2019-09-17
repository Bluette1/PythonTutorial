n = int(input())

a = [['.'] * n for i in range(n)]

# Fill the major diagonal with stars
j = n
for i in range(n):
    j -= 1
    a[i][j] = '*'

# Fill the minor diagonal with stars
j = 0
for i in range(n):
    a[i][j] = '*'
    j += 1

# Fill the vertical middle line with stars
j = n // 2
for i in range(n):
    a[i][j] = '*'

# Fill the horizontal middle line with stars
i = n // 2
for j in range(n):
    a[i][j] = '*'

for i in range(n):
    print(a[i])

