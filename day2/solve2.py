from functools import reduce
import re

with open("day2/input") as file:
    puzzle = file.readlines()

# turns "4 green, 2 blue" into [(4, "green"), (2, "blue")]
def parse_grab(grab):
    cubes = re.findall("(\d+) (\w+)", grab)
    return [(int(x), y) for x, y in cubes]

# from [(4, "green"), (2, "blue"), (2, "green"), (5, "blue")] returns [(4, "green"), (5, "blue")]
def max_each(grabs):
    result = []
    for grab in grabs:
        for color in grab:
            in_result = [(x, y) for x, y in result if y == color[1]]
            if len(in_result) == 0:
                result.append(color)
            elif color[0] > in_result[0][0]:
                result[result.index(in_result[0])] = color # replace that color in result with current count
    return result

answer = 0
for line in puzzle:
    game = re.findall("(?:Game (\d+):)|(?: ([^;]+);?)", line)
    minimum_set = max_each([parse_grab(game[i][1]) for i in range(1, len(game))])
    game_power = reduce(lambda x, y: x * y, [x[0] for x in minimum_set])
    answer += game_power

print(answer)
