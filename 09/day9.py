import copy


def checkNeighbors(arr, i, j):
    sick = 0
    for row, col in neighbors:
        try:
            if arr[i + row][j + col] == 'S':
                sick += 1
        except IndexError:
            pass
    return sick


current_spread = [list(i) for i in open('sicklist.txt').read().split('\n')]
neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
still_spreading = True
days = 0
while still_spreading:
    new_spread = copy.deepcopy(current_spread)
    for i, line in enumerate(current_spread):
        for j, elf in enumerate(line):
            if elf == 'F' and checkNeighbors(current_spread, i, j) >= 2:
                new_spread[i][j] = 'S'
    days += 1
    if new_spread == current_spread:
        still_spreading = False
    else:
        current_spread = new_spread
print(days)
