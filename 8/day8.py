full_list = open('locations.txt', 'r').read().splitlines()

places, route = full_list[:50], full_list[50:]
locations = []

for place in places:
    splitter = place.split(': ')
    coords = [
        int(splitter[1].split(', ')[0][1:]),
        int(splitter[1].split(', ')[1][:-1])
    ]
    name = splitter[0]
    locations.append([name, coords])
print(locations)
