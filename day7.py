with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

# splitter format (row: int, used: boolean = false, visited: int = 0)
splitters = {}
for row, line in enumerate(lines):
    for col, char in enumerate(line):
        if char == '.':
            continue
        if char == '^':
            splitters.setdefault(col, []).append([row, False, -1])
        else:
            start = (row, col)

#print(splitters)
#print(start)
# TODO: Now it only works for second assignment, not first.
def traverse(start):
    for splitter in splitters.get(start[1], []):
        if splitter[0] <= start[0]:
            continue
        #if splitter[1] == True:
        #    # Already handled
        #    return
        splitter[1] = True
        if splitter[2] != -1:
            return splitter[2]
        break
    else:
        #print(f"Found no more splitters {start=}")
        return 1
    global splits
    splits += 1
    splitter[2] = traverse((splitter[0], start[1]-1)) + traverse((splitter[0], start[1]+1))
    return splitter[2]

splits = 0
paths = traverse(start)
print(splits)
print(paths)