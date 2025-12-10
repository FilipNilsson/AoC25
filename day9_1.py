import itertools

with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

points = {}
for line in lines:
    col, row = [int(x) for x in line.split(',', 1)]
    if not points.get(col) or len(points.get(col)) == 1:
        points.setdefault(col, []).append((col, row))
        points[col].sort()
    elif row < points[col][0][1]:
        points[col][0] = (col, row)
    elif points[col][1][1] < row:
        points[col][1] = (col, row)

points = dict(sorted(points.items()))
print(points)
points = [point for values in points.values() for point in values]
print(points)
points_set = set(points)

max_area = 0
for idx, p0 in enumerate(points):
    for jdx, p1 in enumerate(points):
        if jdx <= idx:
            continue
        max_area = max(abs((p1[0] - p0[0] + 1) * (p1[1] - p0[1] + 1)), max_area)
print(max_area)
