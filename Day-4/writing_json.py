import json

with open("person.json", "w") as file:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    person = {"name": name, "age": age}
    json.dump(person, file)