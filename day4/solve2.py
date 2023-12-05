import re

with open("day4/input") as file:
    puzzle = file.readlines()

matches = []
for line in puzzle:
    parsed = re.match("^.+: (.+) \| (.+)$", line)
    winners = parsed.group(1).split()
    haves = parsed.group(2).split()
    matches.append(sum(1 for n in haves if n in winners))

copies_taken_cache = [None] * len(matches)

def get_copies_taken(card):
    if copies_taken_cache[card] != None: return copies_taken_cache[card]
    
    copies_taken = 1
    for n in range(card + 1, min(card + matches[card] + 1, len(matches))):
        copies_taken += get_copies_taken(n)
    
    copies_taken_cache[card] = copies_taken
    return copies_taken

answer = sum(get_copies_taken(card) for card in range(0, len(matches)))
print(answer)