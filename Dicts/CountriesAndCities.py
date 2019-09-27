n = int(input())
countries = {}

for i in range(n):
    line = input().split()
    country = line[0]
    if country not in countries:
        countries[country] = [city for city in line[1:]]

m = int(input())
output = []
for i in range(m):
    city = input()
    for country in countries:
        if city in countries[country]:
            output.append(country)
print(*output)

