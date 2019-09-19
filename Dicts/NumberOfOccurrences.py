dict = {}
out = []
for s in input().split():
    if s not in dict:
        dict[s] = 0
        out.append(0)
    else:
        dict[s] += 1
        out.append(dict[s])

print(*out)
