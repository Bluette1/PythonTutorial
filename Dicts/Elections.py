n = int(input())

dict = {}

for s in range(n):
    candidate, votes = input().split()
    if candidate not in dict:
        dict[candidate] = int(votes)
    else:
        dict[candidate] += int(votes)

for candidate in dict:
    print(candidate, dict[candidate])


