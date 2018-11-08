#Menu Bacteria Analasys - Python Project 1

 
import numpy as np

def inputNumber(prompt):

    while True:
        try:
            num = float(input(prompt))
            break
        except ValueError:
            pass
    return num

def displayMenu(options):
    for i in range(len(options)):
        print("{:d}. {:s}".format(i+1, options[i]))

    choice = 0
    choice = inputNumber("Choose an option from the MENU:")
    while not(np.any(choice == np.arange(len(options))+1)):
        print("Invalid Choice. Enter any key to try again..")
        choice = inputNumber("hoose an option from the MENU:")
    return choice   

loop=True 
while loop:          #The Menu will run until loop = False
    print(15 * "=" , "MENU" , 15 * "=")
    a =["Load Data","Filter Data","Display Statistics","Generate Plots","Quit",]
    choice = displayMenu(a)
    
    if choice==1:     
        print ("Load Data has been selected!")
        #Add code
    elif choice==2:
        print ("Filter Data has been selected!")
        #Add code
    elif choice==3:
        print ("Display Statistics has been selected!")
        #Add code
    elif choice==4:
        print ("Generate Plots has been selected!")
        #Add code
    elif choice==5:
        print ("-Quitting Program-")
        #Add code
        loop=False #Ending whileloop
#Else Any integer inputs other than values 1-5 we print an error message






