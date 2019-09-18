n = int(input())
A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

str = input()
while str != 'HELP':
    B = {int(s) for s in str.split()}
    if input() == 'YES':
        # keep set only B
        A = B
    else:
        # remove all elements of B from A
        A -= B
    str = input()

print(A)
