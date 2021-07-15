
try:   
    number = int(input("Enter number: "))
    result = 1/number
    

except ValueError:
    print("Invalid input. Please enter a number, not a letter: ")
   
except ZeroDivisionError:
    print ("Divided by ZERO!")
   
