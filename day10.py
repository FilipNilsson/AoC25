from itertools import chain, combinations as comb
import z3

with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

total = 0
for line in lines:
    parts = line.split()
    goal = parts[0].strip('[]').replace('#', '1').replace('.', '0')
    goal_value = int(goal, 2)
    start = goal.replace('1', '0')
    switches = [eval(x.replace(')', ',)')) for x in parts[1:-1]]
    for l in range(1, len(switches) + 1):
        for setting in comb(switches, l):
            indices = chain(*setting)
            start_0 = list('0' * len(start))
            for jdx in indices:
                start_0[jdx] = '1' if start_0[jdx] == '0' else '0'
            if int(''.join(start_0), 2) == goal_value:
                total += len(setting)
                break
        else:
            continue
        break
print(total)

total = 0
for line in lines:
    optimizer = z3.Optimize()
    parts = line.split()
    buttons = [eval(x.replace(')', ',)')) for x in parts[1:-1]]
    presses = [z3.Int(f'b{i}') for i in range(len(buttons))]
    optimizer.add(z3.And([button >= 0 for button in presses]))
    joltages = [int(x) for x in parts[-1].strip('{}').split(',')]
    constraints = []
    for i, joltage in enumerate(joltages):
        expr_sum = 0
        for j, button in enumerate(buttons):
            if i in button:
                expr_sum += presses[j]
        constraints.append(expr_sum == joltage)
    optimizer.add(z3.And(constraints))

    optimizer.minimize(sum(presses))
    optimizer.check()
    model = optimizer.model()
    for press in presses:
        total += model[press].as_long()

print(f'{total=}')

