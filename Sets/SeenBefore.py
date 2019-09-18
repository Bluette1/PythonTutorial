A = set()
a =[int(s) for s in input().split()]

for i in range(len(a)):
    if {a[i]} <= A:
        print('YES')
    else:
        print('NO')
        A.add(a[i])