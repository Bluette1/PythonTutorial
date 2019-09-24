n = int(input())
dict = {}

for line in range(n):
    for word in input().split():
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1

# Add key, value pairs to array and then sort using 'sorted which will
# do the sorting by frequency, and then lexicographically if the frequency is the same
output = []
for word in dict:
    output.append([dict[word], word])

print(sorted(output))




