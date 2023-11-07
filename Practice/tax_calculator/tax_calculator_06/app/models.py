import calendar


class Income:
    def __init__(self, year, month, amount = 0) -> None:
        self.year = year
        self.month = month
        self.amount = amount

    def get_month(self):
        return calendar.month_name[self.month]
    
    def get_date_label(self):
        return f"{self.get_month():>9} {self.year}"
    
    def present(self):
        return f"{self.get_date_label()}: {self.amount:.2f}"
    
    def to_dict(self) -> dict:
        return {
            'year': self.year,
            'month': self.month,
            'amount': self.amount,
        }
