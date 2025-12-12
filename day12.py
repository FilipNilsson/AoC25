with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

boxes = []
ok = 0
no = 0
unsure = 0
current_box_being_parsed = [-1, 0, 0, 0]  # idx, width, height, total_hashes
for line in lines:
    if not line:
        assert current_box_being_parsed[1:-1] == [
            7,  # 0x111 = 7 => 3 wide
            3
        ], current_box_being_parsed
        boxes.append(current_box_being_parsed)
        continue

    if line[:-1].isdigit():
        current_box_being_parsed = [line[:-1], 0, 0, 0]
    if line.startswith('#') or line.startswith('.'):
        current_box_being_parsed[3] += line.count('#')
        current_box_being_parsed[2] += 1
        current_box_being_parsed[1] |= int(line.replace('#', '1').replace('.', '0'), 2)

    if 'x' in line:
        dimensions, *box_counts = line.split()
        max_boxes_width, max_boxes_height = [int(x.strip(':'))//3 for x in dimensions.split('x')]
        max_boxes = max_boxes_height * max_boxes_width
        if sum([int(x) for x in box_counts]) <= max_boxes:
            ok += 1
        elif sum([box[3] * int(box_counts[idx]) for idx, box in enumerate(boxes)]) > eval(dimensions[:-1].replace('x', '*')):
            no += 1
        else:
            unsure += 1

print(ok)
assert unsure == 0, 'solution is not valid for the input, or maybe the implementation is wrong'