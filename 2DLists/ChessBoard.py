m, n = input().split(' ')
m, n = int(m), int(n)
a = [[''] * n for i in range(m)]

start_row = '.'
prev = '*'
for i in range(m):
    for j in range(n):
        if prev == '.':
            a[i][j] = '*'
            prev = '*'
        else:
            a[i][j] = '.'
            prev = '.'
    if start_row == '.':
        start_row = '*'
        prev = '.'
    else:
        start_row = '.'
        prev = '*'

for i in range(m):
    print(a[i])

