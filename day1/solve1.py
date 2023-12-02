import re

with open("day1/input") as file:
    puzzle = file.read()

puzzle = re.sub("[^\d\n]", "", puzzle)

answer = 0
for line in puzzle.splitlines():
    answer += int(line[0] + line[-1])

print(answer)