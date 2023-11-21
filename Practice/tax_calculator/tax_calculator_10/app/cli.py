from .calculator import TaxCalculator

class TerminalApp:
    def __init__(self) -> None:
        self.calculator = TaxCalculator()

    def print_help(self):
        print("""
Please select action.
a - add a new income
p - to show all incomes
s - to stats
t - to print tax amount
c - to show bar chart of income
r - reload incomes from database (file)
q - to quit from application""")

    def run(self):
        self.print_help()

        while True:
            try:
                action = input("\nYour action: ")

                if action == 'q':
                    print("See you soon!")
                    break

                elif action == 'a':
                    self.add_income()

                elif action == 'p':
                    self.print_incomes()

                elif action == 's':
                    self.print_stats()
                
                elif action == 't':
                    self.print_tax()
                
                elif action == 'c':
                    self.show_chart()
                
                elif action == 'r':
                    self.reload_incomes()
            except:
                print("Unexpected error! Please check your input or values.")
    
    def add_income(self):
        year = int(input("Year: "))
        month = int(input("Month (1-12): "))
        amount = float(input("Income amount: "))

        self.calculator.add_income(year, month, amount)

    def print_incomes(self):
        incomes = self.calculator.get_incomes()

        if not incomes:
            print("No incomes. Please start adding a new one.")
            return

        for income in incomes:
            print(income.present())

    def print_stats(self):
        stats = self.calculator.get_stats()

        print(f"Minimum income: {stats['min']:.2f}")
        print(f"Maximum income: {stats['max']:.2f}")
        print(f"Average income: {stats['avg']:.2f}")
        print(f"Total income: {stats['total']:.2f}")
    
    def print_tax(self):
        tax_amount = self.calculator.get_tax()

        print(f"Tax to be paid: {tax_amount:0.2f}")

    def show_chart(self):
        chart_data = self.calculator.get_chart_data()

        if not chart_data:
            print("No incomes. Please start adding a new one.")
            return

        for label, amount in chart_data:
            print(f"{label}: {'#' * int(amount // 50)}")

    def reload_incomes(self):
        self.calculator.reload_incomes()
