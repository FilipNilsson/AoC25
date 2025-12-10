from shapely import Polygon

with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

points = []
for line in lines:
    col, row = [int(x) for x in line.split(',', 1)]
    points.append((col, row))

max_area = 0
big_polygon = Polygon(points)
for idx, p0 in enumerate(points):
    for jdx, p1 in enumerate(points):
        if jdx <= idx:
            continue
        area = (abs(p1[0] - p0[0]) + 1) * (abs(p1[1] - p0[1]) + 1)
        if area > max_area:
            polygon = Polygon((p0, (p0[0], p1[1]), p1, (p1[0], p0[1])))
            if big_polygon.contains(polygon):
                max_area = area
print(max_area)
