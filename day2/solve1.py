import re

lines = open("day2/input").readlines()

bag = [(12, "red"), (13, "green"), (14, "blue")]

# turns "4 green, 2 blue" into [(4, "green"), (2, "blue")]
def parse_grab(grab):
    cubes = re.findall("(\d+) (\w+)", grab)
    return [(int(x), y) for x, y in cubes]

# checks if [(4, "green"), (2, "blue")] can be drawn from [(12, "red"), (13, "green"), (14, "blue")]
def is_possible(grab, bag):
    for color in grab:
        in_bag = [x for x, y in bag if y == color[1]]
        if len(in_bag) == 0: return
        if color[0] > in_bag[0]:
            return False
    return True

answer = 0
for line in lines:
    game = re.findall("(?:Game (\d+):)|(?: ([^;]+);?)", line)
    game_id = int(game[0][0])
    if all(is_possible(parse_grab(game[i][1]), bag) for i in range(1, len(game))):
        answer += game_id

print(answer)
