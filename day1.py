with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

current_pos = 50
zeroes = 0

for line in lines:
    direction = 1 if line[0] == 'R' else -1
    magnitude = int(line[1:])
    new_zeroes = magnitude // 100
    magnitude = magnitude % 100
    new_pos = current_pos + direction * magnitude
    if (new_pos < 1 and current_pos != 0) or new_pos > 99:
        new_zeroes += 1
    zeroes += new_zeroes
    current_pos = new_pos % 100
print(zeroes)