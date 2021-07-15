# CLASSES 

# Classes are a blue print 

#Car 
#- model 
#- make 
#- vin 
#- color 
# name of the class should always begin with capital letter 

class Car: 
    def __init__(self, make, model): # constructor/initializers 
        # self allows the properties to be available to the objects 
        self.make = make 
        self.model = model 
        self.vin = ""
        self.color = ""
        self.no_of_cylinders = 2
        self.speed = 0 
        self.current_gear = "N"
    
    def drive(self): 
        print("Car is driving")
        self.speed = 40 
        self.current_gear = "D"

    def change_gear(self, gear): 
        self.current_gear = gear
    
    def accelerate(self): 
        self.speed += 5 

    def park(self): 
        self.speed = 0 
        self.current_gear = "P"

# when we create an object/instance of a Car class we are using the Car blueprint to represent 
# an actual car like Honda, Toyota, Tesla, BMW

# create a car 
car = Car("BMW", "Series 3") # car is an instance/object of the Car class 
print(car.current_gear) # N
car.no_of_cylinders = 4 
car.drive()
print(car.current_gear) # D
car.accelerate() 
print(car.speed)
car.accelerate() 
print(car.speed)

car.change_gear("R")


another_car = Car("Tesla", "X") 
another_car.vin = "3456"
another_car.no_of_cylinders = 6




# Table 
# width is in inches 
class Table: 
    def __init__(self, width, height, material, manufacturer):
        self.width = width
        self.height = height
        self.material = material
        self.manufacturer = manufacturer

table = Table(100, 150, "Wood", "Macys") 


class BankAccount: 
    def __init__(self, account_number, account_holder, account_type, routing_number = "44556"): 
        self.account_number = account_number
        self.balance = 0.0 
        self.account_holder = account_holder
        self.account_type = account_type
        self.routing_number = routing_number
    
         # deposit 
    def deposit(self, amount):
        self.balance += amount 
    
    # withdraw 
    def withdraw(self, amount):
        if self.balance >= amount: 
            self.balance -= amount 

    def transfer_funds(self, amount, destination): 
        # withdraw from source account 
        self.withdraw(amount)
        # deposit to destination account 
        destination.deposit(amount)       

account = BankAccount("ACC1234", "John Doe", "Checking")
account.deposit(100)
account.withdraw(200)
print(f"Account balance: {account.balance}") 

# transfer funds 

# objects are by reference 
# This means that their reference/pointer is passed to other functions 
# And other functions can modify the object and it will reflect in the original object 
source_account = BankAccount("ACC456", "John Doe", "Checking")
source_account.deposit(500)

fake_account = source_account 
fake_account.deposit(50000)

spammers_account = fake_account 
spammers_account.deposit(10000)

print(source_account.balance)

destination_account = BankAccount("ACC789", "Mary Doe", "Checking")
source_account.transfer_funds(100, destination_account)

print(source_account.balance) # 400
print(destination_account.balance) # 100

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

# One user can have many addresses 
user = User("John", "Doe")
address = Address("1200 Richmond Ave", "Houston", "TX")

user.add_address(address)
user.add_address(Address("1345 Harvin Ave", "Austin", "TX"))

for address in user.addresses: 
    print(address.street)
    print(address.state)


    
class Post: 
    def __init__(self, title, description, author): 
        self.title = title 
        self.description = description 
        self.author = author 
        self.comments = [] 

class Comment:
    def __init__(self, title, content): 
        self.title = title 
        self.content = content 

         

