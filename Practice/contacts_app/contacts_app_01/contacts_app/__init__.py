from contacts_app.service import ContactsService


__version__ = "0.1"
__app_name__ = "Contacts App"


class ContactsApp:
    def __init__(self, service=None) -> None:
        self.service = service or ContactsService()

    def print_help(self):
        help_text = """
Avaliable actions:
- *a* - add a new customer
- *p* - show all customers
- *q* - quit from application"""

        print(help_text)

    def run(self):
        print(f"Welcome to {__app_name__}/{__version__}")
        self.print_help()

        choices = ('a', 'p', 'q')

        while True:
            try:
                action = input("\nPlease type your action: ")

                if action == 'q':
                    print("See you soon!")
                    break

                if action == 'p':
                    self.print_customers()
                    continue

                if action == 'a':
                    self.add_customer()
                    continue

                print("Unknown option!")
            except:
                print("Unexpected error! Please check your input or values.")
    
    def print_customers(self):
        customers = self.service.get_customers()

        for customer in customers:
            print("{}: {} {} ({}, {})".format(
                customer.id,
                customer.first_name,
                customer.last_name,
                customer.email,
                customer.date_of_birth or '-'
            ))

    def add_customer(self):
        first_name = input("First name: ")
        last_name = input("Last name: ")
        email = input("Email: ")
        date_of_birth = input("Date of birth (optional): ")

        self.service.add_customer({
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "date_of_birth": date_of_birth,
        })
        print("Customer has been added")
