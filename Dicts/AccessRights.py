n = int(input())

access_rights = {}

operations = {'read': 'R', 'write': 'W', 'execute': 'X'}

for i in range(n):
    line = input().split()
    file = line[0]
    access_rights[file] = []
    for j in range(1, len(line)):
        access_rights[file].append(line[j])


m = int(input())
output = []
for i in range(m):
    operation, file = input().split()
    if operations[operation] in access_rights[file]:
        output.append('OK')
    else:
        output.append('Access denied')
for s in output:
    print(s)