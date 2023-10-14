numbers = [10, 12, 9, 10, 15]

cur_idx = 0
while cur_idx < len(numbers):
    print(numbers[cur_idx], end=" ")
    cur_idx += 1

print()

# but better
for number in numbers:
    print(number, end=" ")
