n = int(input())

dict = {}

for s in range(n):
    key, value = input().split()
    dict[key] = value

synonym = input()
for word in dict:
    if dict[word] == synonym:
        print(word)
