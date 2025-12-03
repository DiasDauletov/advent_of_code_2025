# https://adventofcode.com/2025/day/3#part2
import sys
import functools

banks = [[int(digit) for digit in line.rstrip('\n')] for line in sys.stdin]

@functools.cache
def find_max_joltages(cur_joltage_pos, joltages_len, bank_index):
    
    if cur_joltage_pos == -1 or joltages_len == 0:
        return 0
    
    cur_joltage = banks[bank_index][cur_joltage_pos]
    last_is_cur = cur_joltage

    for joltage_pos in range(cur_joltage_pos):
        last_is_cur = max(
            find_max_joltages(joltage_pos, joltages_len - 1, bank_index) * 10 + cur_joltage,
            last_is_cur
        )

    return max(last_is_cur, find_max_joltages(cur_joltage_pos - 1, joltages_len, bank_index))

sum = 0

for index in range(len(banks)):
    sum += find_max_joltages(len(banks[index]) - 1, 12, index)

print(sum)