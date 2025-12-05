with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

for idx, line in enumerate(lines):
    lines[idx] = '.' + line + '.'
lines.insert(0, '.' * len(lines[0]))
lines.append('.' * len(lines[0]))


tmp = lines
total = 0
sub_total = 1
while sub_total != 0:
    sub_total = 0
    for row in range(1, len(lines)-1):
        for col in range(1, len(lines[0])-1):
            if lines[row][col] == '@':
                window = lines[row-1][col-1:col+2] + lines[row][col-1:col+2] + lines[row+1][col-1:col+2]
                if window.count('@') < 5:
                    tmp[row] = lines[row][:col] + '.' + lines[row][col+1:]
                    sub_total += 1
    lines = tmp
    total += sub_total
print(total)