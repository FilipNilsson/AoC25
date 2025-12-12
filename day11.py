from functools import cache

with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

mapping = {}
for line in lines:
    key, *values = line.split()
    key = key[:-1]
    mapping[key] = values

@cache
def resolve(values, contains_dac=False, contains_fft=False):
    if values == 'dac':
        contains_dac = True
    if values == 'fft':
        contains_fft = True
    values = mapping[values]
    if 'out' in values:
        if contains_dac and contains_fft:
            return 1
        else:
            return 0
    total = 0
    for value in values:
        total += resolve(value, contains_dac, contains_fft)
    return total

#print(resolve('you'))  # just always return 1 if hitting out
print(resolve('svr'))
