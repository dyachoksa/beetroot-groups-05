from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel
from rich.columns import Columns
from rich.console import Group

from .calculator import TaxCalculator

class TerminalApp:
    def __init__(self) -> None:
        self.calculator = TaxCalculator()
        self.console = Console()

    def print_help(self):
        help_text = """
Please select action.
- *a* - add a new income
- *p* - to show all incomes
- *s* - to stats
- *t* - to print tax amount
- *c* - to show bar chart of income
- *r* - reload incomes from database (file)
- *q* - to quit from application"""

        md = Markdown(help_text)
        panel = Panel(md, expand=False)
        self.console.print(panel)

    def run(self):
        self.print_help()

        choices = ['a', 'p', 's', 't', 'c', 'r', 'q']

        while True:
            try:
                action = Prompt.ask("Your action", choices=choices)

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
            self.console.print("[cyan]No incomes. Please start adding a new one.[/cyan]")
            return
        
        table = Table(title="My Incomes")

        table.add_column("Year", justify="right", style="cyan")
        table.add_column("Month")
        table.add_column("Income", justify="right", style="green")

        for income in incomes:
            table.add_row(str(income.year), income.get_month(), f"{income.amount:.2f}")

        total = self.calculator.get_total_income()
        table.add_section()
        table.add_row(None, "Total", f"{total:.2f}")
        
        self.console.print(table)

    def print_stats(self):
        stats = self.calculator.get_stats()

        columns = Group(
            Columns(("Minimum income", f"{stats['min']:.2f}")),
            Columns(("Maximum income", f"{stats['max']:.2f}")),
            Columns(("Average income", f"{stats['avg']:.2f}")),
            Columns(("Total income", f"{stats['total']:.2f}")),
        )

        panel = Panel(columns)
        
        self.console.print(panel)
    
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
