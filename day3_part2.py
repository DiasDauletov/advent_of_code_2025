# https://adventofcode.com/2025/day/3#part2
import sys
import functools


# F(I, K) - finds a maximum number with lenth K that can be formed from an array A[0...I],
# e.g. A = [9, 1, 9, 8], I = 2, K = 2 then F(I, K) = 99 
# A contains only digits,  0 <= I, K < len(A)
#
# Solution: F(I, K) = max(F(I - 1, K - 1) + A[I], F(I - 1, K))
#
# In the implementation below: F = find_max_joltages, I = cur_joltage_pos, K = joltages_len, A = banks[bank_index].

banks = [[int(digit) for digit in line.rstrip('\n')] for line in sys.stdin]

@functools.cache
def find_max_joltages(cur_joltage_pos, joltages_len, bank_index):
    if cur_joltage_pos == -1 or joltages_len == 0:
        return 0

    cur_joltage = banks[bank_index][cur_joltage_pos]

    return max(
        find_max_joltages(cur_joltage_pos - 1, joltages_len - 1, bank_index) * 10 + cur_joltage,
        find_max_joltages(cur_joltage_pos - 1, joltages_len, bank_index)
    )

sum = 0
for index in range(len(banks)):
    sum += find_max_joltages(len(banks[index]) - 1, 12, index)

print(sum)