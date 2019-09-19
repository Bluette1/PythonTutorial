n = int(input())
dict = {}
max = 0
most_common = ''
for line in range(n):
    for word in input().split():
        if word not in dict:
            dict[word] = 0
        else:
            dict[word] += 1

# Do another iteration through array to check the most common word such that it is lower in
# alphabetical order
for word in sorted(dict):
    if dict[word] > max:
        max = dict[word]
        most_common = word

print(most_common)

