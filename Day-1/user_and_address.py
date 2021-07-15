class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.addresses = []

    def add_address(self, address):
        self.addresses.append(address)


class Address:
    def __init__(self, street, city, state):
        self.street = street
        self.city = city
        self.state = state
    
person1 = User("Jen", "Ine")
person1.addresses = []



ga_address = Address("Grist Mill", "Peachtree Corners", "Georgia")
dc_address = Address("Sherman Ave", "Washington", "DC")


person1.add_address(ga_address)
person1.add_address(dc_address)

for address in person1.addresses:
    print(address.street)
    print(address.city)
    print(address.state)


