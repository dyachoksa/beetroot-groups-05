from datetime import datetime

name = input("What's your name? ")
print("Welcome, {}!".format(name))
print("Today is {}".format(datetime.now().strftime("%c")))
print("Please provide your income and we will calculate tax for you.")
print("You can type several numbers splitted by space.")
print("To finish just type 'end'.")

income = []

while True:
    amount = input("Income amount ('end' to finish): ")

    if amount == 'end':
        break

    amounts = amount.split(" ")

    income.extend(map(float, amounts))

total_income = 0
common_expected = 100
more_than_common = 0

for amount in income:
    total_income += amount

    if amount > common_expected:
        more_than_common += 1

# or we can as user about it
tax = 13

tax_amount = (tax / 100) * total_income

min_income = min(income)
max_income = max(income)
avg_income = sum(income) / len(income)

print("Your income list: ", income)
print("Recieved more than in common {} time(s)".format(more_than_common))
print(f"Minimun income {min_income:.2f}")
print(f"Maximum income {max_income:.2f}")
print(f"Average income {avg_income:.2f}")
print("Your total income: {:.2f}".format(total_income))
print("Tax amount to pay: {:.2f}".format(tax_amount))
print(f"Tax persent: {tax:.2f}%")

# Simple bar graph
print("\nIncome chart:")
for amount in income:
    size = int(amount // 10)
    print('#' * size)
