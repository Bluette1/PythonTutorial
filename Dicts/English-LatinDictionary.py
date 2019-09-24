n = int(input())
e_l_dict = {}

# Create English-Latin dictionary
for line in range(n):
    entry = input().split(' - ')
    e_l_dict[entry[0]] = [s for s in entry[1].split(', ')]

# Create Latin-English dictionary
l_e_dict = {}
for entry in e_l_dict:
    for word in e_l_dict[entry]:
        if word not in l_e_dict:
            l_e_dict[word] = [entry]
        else:
            l_e_dict[word].append(entry)

# Add key, value pairs to array and then sort using 'sorted which will
# do the sorting lexicographically on key -> value pairs
output = []
for word in l_e_dict:
    output.append([word, l_e_dict[word]])
output = sorted(output)
for entry in output:
    print(entry[0], '-', ', '.join(sorted(entry[1])))



