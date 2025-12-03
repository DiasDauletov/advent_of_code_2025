# https://adventofcode.com/2025/day/3
import sys

banks = [line.rstrip('\n')[::-1] for line in sys.stdin]
sum = 0

for bank in banks:
    max_joltage = bank[1]
    second_max_joltage = bank[0]
    for joltage in bank[2:]:
        if joltage >= max_joltage:
            if max_joltage >= second_max_joltage:
                second_max_joltage = max_joltage
            max_joltage = joltage
    sum += int(max_joltage + second_max_joltage)

print(sum)
    