import re
import math

with open('input.txt', 'r') as file:
    lines = file.read().split(',')

assignment = 2
total = 0

if assignment == 1:
    for line in lines:
        first_str, last_str = line.split('-', 1)
        start = int(first_str)
        end = int(last_str)
        if len(first_str) % 2 == 1:
            first_str = str(int('1' + first_str) - int(first_str))
        if len(last_str) % 2 == 1:
            last_str = '9' * (len(last_str) - 1)
        number = first_str[:len(first_str)//2]
        while True:
            if start <= int(number + number) <= end:
                total += int(number + number)
            elif int(number + number) > end:
                break
            number = str(int(number) + 1)

if assignment == 2:
    from time import perf_counter
    t0 = perf_counter()
    for line in lines:
        first_str, last_str = line.split('-', 1)
        start = int(first_str)
        end = int(last_str)
        numbers = range(start, end+1)
        for number in numbers:
            # The regex is enough, but early exits speed it up by a lot
            sub_str = str(number)
            unique = len(set(sub_str))
            if unique > len(sub_str) // 2:
                continue
            if unique == 1:
                total += number
                continue
            if re.findall(r'^(\d+)\1+$', str(number)):
                total += number
    print(perf_counter() - t0)
print(total)