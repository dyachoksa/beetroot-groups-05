from datetime import datetime

name = input("What's your name? ")
print("Welcome, {}!".format(name))
print("Today is {}".format(datetime.now().strftime("%c")))
print("Please provide your income and we will calculate tax for you.")
print("To finish just type 'end'.")

total_income = 0

while True:
    amount = input("Income amount ('end' to finish): ")

    if amount == 'end':
        break

    total_income += float(amount)

# or we can as user about it
tax = 13

tax_amount = (tax / 100) * total_income

print("Your total income: {:.2f}".format(total_income))
print("Tax amount to pay: {:.2f}".format(tax_amount))
print(f"Tax persent: {tax:.2f}%")
