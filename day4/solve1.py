import re

with open("day4/input") as file:
    puzzle = file.readlines()

answer = 0
for line in puzzle:
    parsed = re.match("^.+: (.+) \| (.+)$", line)
    winners = parsed.group(1).split()
    haves = parsed.group(2).split()
    matches = sum(1 for n in haves if n in winners)
    score = 0 if matches == 0 else 2 ** (matches-1)
    answer += score

print(answer)