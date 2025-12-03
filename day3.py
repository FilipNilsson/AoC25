with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

slots = 12 # 2 for assignment 1
total = 0
for line in lines:
    amount = list(line[-slots:])
    for char in reversed(line[:-len(amount)]):
        if char >= amount[0]:
            tmp = amount.copy()
            amount[0] = char
            for idx, _ in enumerate(tmp[1:]):
                if tmp[idx] >= tmp[idx+1]:
                    amount[idx+1] = tmp[idx]
                else:
                    break
    total += int(''.join(amount))
print(total)