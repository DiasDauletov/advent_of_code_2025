# https://adventofcode.com/2025/day/2#part2
import math

# Parse input ranges that are in this format: 11-22,95-115,998-1012,1188511880-1188511890...
ranges = [(int(pair[0]), int(pair[1])) for pair in 
    [range.split('-') for range in input().split(',')]
]

invalid_numbers = set()
for num in range(1, int(1e5)):
    num_length = int(math.log10(num)) + 1
    max_times = 10 // num_length

    for times in range(2, max_times + 1):
        invalid_numbers.add(int(str(num) * times))

result = 0

for (left, right) in ranges:
    result += sum([num for num in invalid_numbers if num >= left and num <= right])

print(result)