import re
from functools import cache

with open("day4/input") as file:
    puzzle = file.readlines()

matches = []
for line in puzzle:
    parsed = re.match("^.+: (.+) \| (.+)$", line)
    winners = parsed.group(1).split()
    haves = parsed.group(2).split()
    matches.append(sum(1 for n in haves if n in winners))

@cache
def get_copies_taken(card):    
    copies_taken = 1
    for n in range(card + 1, min(card + matches[card] + 1, len(matches))):
        copies_taken += get_copies_taken(n)
    return copies_taken

answer = sum(get_copies_taken(card) for card in range(0, len(matches)))
print(answer)