# https://adventofcode.com/2025/day/2

# Parse input ranges that are in this format: 11-22,95-115,998-1012,1188511880-1188511890...
ranges = [(int(pair[0]), int(pair[1])) for pair in 
    [range.split('-') for range in input().split(',')]
]

invalid_numbers = [int(str(num) * 2) for num in range(1, int(1e5))]
result = 0

for (left, right) in ranges:
    result += sum([num for num in invalid_numbers if num >= left and num <= right])

print(result)