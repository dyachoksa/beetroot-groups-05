user_numbers = input("Please enter a list of numbers separated by space: ")

numbers = user_numbers.split(" ")

prev_number = 0
for number in numbers:
    try:
        number = int(number)

        print(f"{prev_number=} / {number=} = {prev_number/number}")

        prev_number = int(number)
    except ZeroDivisionError:
        print("Can't divide by 0. Skipping...")
    except ValueError:
        print("Not an integer. Skipping...")
        # print("Unexpected value. Stopping...")
        # break

print("Finished")
