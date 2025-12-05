with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

ranges = []
for range_idx, line in enumerate(lines):
    if not line:
        break
    start, end = [int(i) for i in line.split('-')]
    idx_to_remove = []
    for idx, (range_start, range_end) in enumerate(ranges.copy()):
        if range_start <= start <= range_end or range_start <= end <= range_end:
            end = max(range_end, end)
            start = min(range_start, start)
            del ranges[idx]
    ranges.append((start, end))

len_ranges = -1
while len_ranges != len(ranges):
    len_ranges = len(ranges)
    ranges_copy = ranges.copy()
    for idx, range in enumerate(ranges_copy):
        start, end = range
        for jdx, other_range in enumerate(ranges_copy):
            if idx == jdx:
                continue
            if other_range[0] <= range[0] <= other_range[1] or other_range[0] <= range[1] <= other_range[1]:
                end = max(range_end, range[1])
                start = min(range_start, range[0])
                try:
                    del ranges[max(idx, jdx)]
                    del ranges[min(jdx, idx)]
                except:
                    breakpoint()
                    pass
        ranges.append((start, end))
    print(f'Removed {len_ranges - len(ranges)} ranges')
    

for idx, range in enumerate(ranges):
    for jdx, other_range in enumerate(ranges):
        if idx == jdx:
            continue
        if other_range[0] <= range[0] <= other_range[1] or other_range[0] <= range[1] <= other_range[1]:
            print(f'{idx} {range=} - {jdx} {other_range=}')

total_2 = 0
for range in ranges:
    total_2 += (range[1] - range[0]) + 1
print(total_2)

total_1 = 0
for line in lines[range_idx+1:]:
    for range in ranges:
        if range[0] <= int(line) <= range[1]:
            total_1 += 1
            break
print(total_1)