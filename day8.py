import math

with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

points = []
for line in lines:
    points.append([int(x) for x in line.split(',')])

distances = []
for idx, first in enumerate(points):
    for jdx, second in enumerate(points):
        if jdx <= idx:
            continue
        distances.append((math.sqrt(
            pow(second[0] - first[0], 2) + pow(second[1] - first[1], 2) + pow(second[2] - first[2], 2)),
        idx, jdx))

distances.sort()
#distances = distances[:1000]
circuits: list[set] = []
for pair in distances:
    #if pair[1:] == (10, 12):
    #    breakpoint()
    one_set = False
    two_set = False
    for junction in circuits:
        if pair[1] in junction and pair[2] in junction:
            one_set = True
            two_set = True
            break
        if not one_set and pair[1] in junction:
            junction.add(pair[2])
            one_set = junction
            if two_set:
                junction.update(two_set)
                circuits.remove(two_set)
            if len(junction) == len(points):
                print(f'All connected {pair=} | {points[pair[1]]} {points[pair[2]]}')
                print(points[pair[1]][0] * points[pair[2]][0])
                exit()
        elif not two_set and pair[2] in junction:
            junction.add(pair[1])
            two_set = junction
            if one_set:
                junction.update(one_set)
                circuits.remove(one_set)
            if len(junction) == len(points):
                print(f'All connected {pair=} | {points[pair[1]]} {points[pair[2]]}')
                print(points[pair[1]][0] * points[pair[2]][0])
                exit()
    if not one_set and not two_set:
        circuits.append({pair[1], pair[2]})
    #print(f'{circuits} {pair[1:]} ')

circuits.sort(key=len, reverse=True)
print(circuits)
print(len(circuits[0]) * len(circuits[1]) * len(circuits[2]))