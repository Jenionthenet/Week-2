import json



users = []

while True:
        
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    person_dict = {"name": name, "age": age}
    users.append(person_dict)

    with open("users.json", "w") as file:
        json.dump(users, file)

    option = input("q to quit or any key to continue ")
    if option == "q":
         break

with open("users.json")as file:
    users = json.load(file)
    
for user in users:
    print(f" Name: {user['name']}, Age: {user['age']}")
    

    
