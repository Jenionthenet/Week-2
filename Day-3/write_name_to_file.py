file = open("guest.txt", "w")
name = input("Please enter your first and last name: ")
file.write(name)
file.close()