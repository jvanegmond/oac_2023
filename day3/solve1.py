import re

with open("day3/input") as file:
    puzzle = file.readlines()

answer = 0
for y in range(0, len(puzzle)):
    line = puzzle[y]
    
    num = ""
    for x in range(0, len(line)):
        ch = line[x]
        if ch.isdigit():
            num += ch
        elif len(num) > 0:
            search_space = ""
            for sy in range(max(y - 1, 0), min(y + 2, len(puzzle))):
                for sx in range(max(x - len(num) - 1, 0), min(x + 1, len(line) - 1)):
                    search_space += puzzle[sy][sx]
                search_space += "\n"
            if re.search("[^\.\d\\n]", search_space):
                answer += int(num)
            num = ""

print(answer)