class Customer:
    def __init__(self, first_name, last_name, email, date_of_birth=None, customer_id=None):
        self.id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.date_of_birth = date_of_birth

        self.addresses = []
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Address:
    def __init__(self, city, post_code, address, is_shipping=True):
        self.id = None
        self.city = city
        self.post_code = post_code
        self.address = address
        self.is_shipping = is_shipping

        self.customer = None
    
    def __str__(self) -> str:
        return "{} {}, {}".format(self.post_code, self.city, self.address)
