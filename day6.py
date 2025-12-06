import numpy as np

with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

'''Part B'''
for col, char in enumerate(lines[-1][1:]):
    if char != ' ':
        for row, line in enumerate(lines[:-1]):
            lines[row] = lines[row][:col] + '-' + lines[row][col+1:]

for idx, line in enumerate(lines[:-1]):
    lines[idx] = line.split('-')
lines[-1] = lines[-1].split()

rows = len(lines) - 2
m = np.array(lines)
m = np.rot90(m)

big_total = 0
for part in m:
    operation = part[-1]
    total = 1 if operation=='*' else 0
    for idx, col in enumerate(part[0]):
        number = int(''.join([part[x][idx] for x in range(0, rows+1)]).strip())
        if operation == '*':
            total *= number
        else:
            total += number
    big_total += total
print(big_total)

'''Part A'''
"""operations = lines[-1].split()
results = [1 if op=='*' else 0 for op in operations]
for line in lines[:-1]:
    for idx, value in enumerate(line.split()):
        if operations[idx] == '*':
            results[idx] = results[idx] * int(value)
        else:
            results[idx] = results[idx] + int(value)
print(sum(results))"""
