# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 21:38:47 2018

@author:
"""
import numpy as np
#Initial variables
dataLoaded = False
conditions = ["No active bacteria filter","No active GR filter","No active temp filter",np.array([],dtype=int),None,None]

#Keep menu until user quits
while True:
    header("MAIN MENU") #Interface
    printFilter(conditions[0],conditions[1],conditions[2]) #Print any active filters
    #User Menu
    menu = displayMenu(["Load data","Filter data","Display statistics", "Generate plots", "Show data", "Quit"])
    
    #Load data
    if menu == 1:
        #Checks for a valid filename
        header("LOAD DATA MENU") #Header
        print("type 'exit, if you wish to exit'")
        while True:
            try:
                filename = inputStr("Please enter the name of your datafile: ")
                print("") #Add space
                
                #Check for exit
                if filename.lower() != "exit":
                    data = dataLoad(filename) #Loads the data
                    print("\nData was succesfully loaded from",filename)
                    dataLoaded = True # Set data as loaded
                    dataOld = np.copy(data) #Makes a copy of our data
                    break
                
                #Exits
                else:
                    break
                
            except FileNotFoundError:
                print("File could not be found, please try again")
    
    #Goes into filter data menu
    elif (menu == 2) and dataLoaded:
        while True:
            header("FILTER MENU") #Header
            print("Choose one of the filters")
            #Prints active filters
            printFilter(conditions[0],conditions[1],conditions[2])
            
            menu2 = displayMenu(["Bacteria filter","Growth rate filter","Temperature filter","Back"])
            
            #Bacteria type filter
            if menu2 == 1:
                data,conditions = filterData("Bacteria filter",data,dataOld,conditions)
                
            #GR filter
            elif menu2 == 2:
                data,conditions = filterData("Growth rate filter",data,dataOld,conditions)
            
            #Temp filter 
            elif menu2 == 3:
                data,conditions = filterData("Temperature filter",data,dataOld,conditions)
            
            #Back
            elif menu2 == 4:
                break
                        
    
    #Display statistics
    elif (menu == 3) and dataLoaded:
        statStr = ["meanTemp","meanGR","stdTemp","stdGR", "rows","meanCGR", "meanHGR","Back"]
        
        header("STATISTICS MENU") # Header for statistics
        #Prints active filters 
        printFilter(conditions[0],conditions[1],conditions[2])
        while True:   
            menu2 = displayMenu(statStr) #Show different statistics to be computed
            if menu2 == 8: #exit
                break
            else:
                stat = dataStatistics(data,statStr[int(menu2-1)]) #Compute statistic
           
            #Prints any active filters
            printFilter(conditions[0],conditions[1],conditions[2])
            
            #Print statistic
            print("""\n==================================================   
{}
--------------------------------------------------
{}
==================================================\n""".format(statStr[int(menu2-1)],stat))
            
            
    # Generates your current plot
    elif (menu == 4) and dataLoaded:
        dataPlot(data)
        print("")
    
    #Shows your current data
    elif (menu == 5) and dataLoaded:
        np.set_printoptions(threshold=np.inf)
        np.set_printoptions(suppress=True)
        print(data)
        np.set_printoptions(threshold=8)
        
        
    #Quit
    elif menu == 6:
        break
    
    #If no data has been loaded display this error. 
    else:
        print("ERROR: No data has been loaded, Please load your data using option 1")