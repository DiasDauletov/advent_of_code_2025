# https://adventofcode.com/2025/day/1

dial = 50
counter = 0

while True:
    # {L,R} + number of rotations
    text = input()
    if text == "":
        break
    direction = text[0]
    num_of_rotations = int(text[1:])

    dial += num_of_rotations if direction == 'R' else -num_of_rotations
    dial %= 100

    if dial == 0:
        counter += 1

print(counter)