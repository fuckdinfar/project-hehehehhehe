import numpy as np
# the following functions are meant as helping functions for the main script taking user input and displaying headers.
def header(headerString):

    print("""
====================
{}
====================\n""".format(headerString))

def inputStr(prompt):   
    while True:
        try:
            str = input(prompt)
            break
        except ValueError:
            print("Not a valid input. Please try again")
    return str

def inputNumber(prompt):
    while True:
        try:
            num = float(input(prompt))
            break
        except ValueError:
            print("Not a valid input. Please try again")
    return num

def inputLimit(prompt):
    while True:
        try:
            num = input(prompt) #Get input
            num = float(num) #Tries to convert it to a float value.
            break
        except ValueError:
            if num == "clear": #If input is clear then break
                num = "clear"
                break
            elif num == "back":
                num = "back"
                break
            else:    
                print("Not a valid input. Please try again")
    return num

def displayMenu(options):
    #Print menu
    for i in range(len(options)):
        print("{}. {}".format(i+1,options[i]))
    
    #Initial variable
    choice = 0
    
    #Get menu choice
    while not choice in np.arange(1,len(options)+1):
        choice = inputNumber("Please choose a menu item: ")
        if choice > len(options) or choice <= 0:
            print("\nChoice out of menu range")

    return choice