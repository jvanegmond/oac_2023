import re

with open("day3/input") as file:
    puzzle = file.readlines()

gear_nums = []
for y in range(0, len(puzzle)):
    line = puzzle[y]
    
    num = ""
    for x in range(0, len(line)):
        ch = line[x]
        if ch.isdigit():
            num += ch
        elif len(num) > 0:
            # look for *gear* in search space
            for sy in range(max(y - 1, 0), min(y + 2, len(puzzle))):
                for sx in range(max(x - len(num) - 1, 0), min(x + 1, len(line) - 1)):
                    if puzzle[sy][sx] == "*": gear_nums.append((sy, sx, int(num)))
            num = ""

answer = 0
gear_nums.sort()
for n in range(0, len(gear_nums) - 1):
    gear1 = gear_nums[n]
    gear2 = gear_nums[n+1]
    if gear1[0] == gear2[0] and gear1[1] == gear2[1]:
        answer += gear1[2] * gear2[2]

print(answer)