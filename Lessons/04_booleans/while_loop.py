letter = "*"

num_times = 10
current = 1

while current <= num_times:
    print(letter * current)

    if current % 2 == 0:
        print("#" * current)

    current += 1
else:
    print("Loop completed")

while True:
    print(1)
    break

print("Done!")
