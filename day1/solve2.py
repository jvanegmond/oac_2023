import re

with open("day1/input") as file:
    puzzle = file.read()

numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
def letters_to_number(num):
    if len(num) == 1: return num
    return str(numbers.index(num))

pattern = "(\d|" + str.join("|", numbers) + ")"

answer = 0
for line in puzzle.splitlines():
    first = letters_to_number(re.match("(?:.*?)" + pattern, line).group(1))
    last = letters_to_number(re.match("(?:.*)" + pattern, line).group(1))
    answer += int(first + last)

print(answer)