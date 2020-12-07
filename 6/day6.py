def sumArray(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum


packs = list(map(int, open('candy.txt', 'r').read().split(',')))
elves = 127
total_packs = len(packs)
total_candy = sumArray(packs)

for i in range(total_packs - 1, 0, -1):
    if total_candy % elves != 0:
        total_candy -= packs[i]
    else:
        candy = total_candy / elves

print(candy)
