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
            idx_to_remove.append(idx)
    idx_to_remove.sort(reverse=True)
    for idx in idx_to_remove:
        del ranges[idx]
    ranges.append((start, end))

needs_fixing = [True]
while needs_fixing:
    needs_fixing = []
    for idx, range in enumerate(ranges):
        for jdx, other_range in enumerate(ranges):
            if idx == jdx:
                continue
            if other_range[0] <= range[0] <= other_range[1] or other_range[0] <= range[1] <= other_range[1]:
                needs_fixing.append(idx)

    for idx in needs_fixing:
        start, end = ranges[idx]
        idx_to_remove = []
        for jdx, (other_start, other_end) in enumerate(ranges):
            if jdx == idx:
                continue
            if other_start <= start <= other_end or other_start <= end <= other_end:
                end = max(other_end, end)
                start = min(other_start, start)
                idx_to_remove.append(jdx)
        ranges[idx] = (start, end)
        idx_to_remove.sort(reverse=True)
        for jdx in idx_to_remove:
            del ranges[jdx]

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