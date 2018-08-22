print("Welcome to this calculator which is fully built in Python")
print("These are the sybols; Multiply: *, Exponent: **, Subtract: -, Addition: +, Division: /")
user =  input("What operation would you like to do: ")

if user == "*":
    FMulti = int(input("What is the first number you would like to MULTIPLY: "))
    SMulti = int(input("What would you like the first number to be MULTIPLIED BY: "))
    Multipli = (FMulti * SMulti)
    print(Multipli)
elif user == "-": 
    FSub = int(input("What is the first number you would like to SUBTRACT: "))
    SSub = int(input("What would you like the first number to be SUBTRACT BY: "))
    Suby = (FSub - SSub)
    print(Suby)
elif user == "+":
    FAd = int(input("What is the first number you would like to ADD: "))
    SAd = int(input("What would you like to add to the first number: "))
    Addy = (FAd + SAd)
    print(Addy)
elif user == "/":
    FDiv = int(input("What is the first number you would like to DIVIDE: "))
    SDiv = int(input("What would you like this number to be DIVIDED BY: "))
    Divy = (FDiv / SDiv)
    print(Divy)
elif user == "**":
    FPow = int(input("What number would you like to be the BASE: "))
    SPow = int(input("What would you like to be the EXPONENT: "))
    Powy = (FPow ** SPow)
    print(Powy)
else:
    Nothin = print(" You didn't enter an operation :( ")
print("|-----------------------------------------------------|")
print("|                                                     |")
print("|                                                     |")
print("|                                                     |")
print("|                 Created by Benny:)                  |")
print("|                                                     |")
print("|                                                     |")
print("|                                                     |")
print("|-----------------------------------------------------|")
print('This program is finsihed')




