from contacts_app.models import Customer
from contacts_app.store import DatabaseStore


class ContactsService:
    def __init__(self, store=None) -> None:
        self.store = store or DatabaseStore()
    
    def get_customers(self):
        return self.store.get_customers()
    
    def add_customer(self, data: dict):
        required_fields = ("first_name", "last_name", "email")
        for field in required_fields:
            if (field not in data) or (data.get(field) is None) or (not data[field].strip()):
                raise ValueError(f"{field.capitalize()} is required")
            
        customer = Customer(
            first_name=data["first_name"].strip(),
            last_name=data["last_name"].strip(),
            email=data["email"].strip().lower(),
            date_of_birth=data["date_of_birth"].strip()
        )

        self.store.insert_customer(customer)
