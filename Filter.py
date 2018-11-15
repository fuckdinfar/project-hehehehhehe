# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 21:37:08 2018

@author: Bruger
"""

import numpy as np
def printFilter(bacActive,growthActive,tempActive):
# Help functions which filters the data. 
    
    if (type(bacActive) == np.ndarray) or (type(growthActive) == list) or (type(tempActive) == list): 
    #Print active filters if any
        print("""=======================================================
                     ACTIVE FILTERS
         
Current filters:
Bacteria: {} 
Growth rate range: {}
Temperature range: {}
=======================================================
                      """.format(bacActive,growthActive,tempActive))
    

def filterData(filtertype,data,dataOld,conditions):

    #Initial variables
    bacStr = ["Salmonella enterica","Bacillus cereus","Listeria",
          "Brochothrix thermosphacta"]
    r1,r2 = None,None
    
    #Extracting variables from condition list
    bacActive = conditions[0] #Active bacteria filters
    growthActive = conditions[1] #Active range filters
    tempActive = conditions[2]#Active temperature filter
    bacList = conditions[3] #Array of bacteria types, integers
    range_ = conditions[4] #Boolean array where range was true
    mask = conditions[5] #Boolean array where bacList is in data
        
    #Growth rate range filter    
    if filtertype == "Growth rate filter":
        header("GROWTH RATE FILTER MENU") #Interface
        print("""You have chosen to filter for growth rate range.
Type "clear" to clear range or "back" to go back""")
        
        while True:
            r1 = inputLimit("Please enter a lower limit: ") 
            #Break if clear
            if r1 == "clear":
                growthActive = "No active GR filter"
                break
            #Exit without changing anything
            elif r1 == "back":
                break
            
            r2 = inputLimit("Please enter an upper limit: ")
            #Break if clear
            if r2 == "clear":
                growthActive = "No active GR filter"
                break
            #Exit without changing anything
            elif r2 == "back":
                break
                
            #Puts the values in correct order
            growthActive = [min(r1,r2),max(r1,r2)]
            break
        
    #Temperature range filter     
    elif filtertype == "Temperature filter":
        header("TEMPERATURE FILTER MENU") #Interface
        print("""You have chosen to filter for temperature.
Type "clear" to clear range and "back" to go back""")
        
        while True:
            r1 = inputLimit("Please enter a lower limit: ") 
            #Break if clear
            if r1 == "clear":
                tempActive = "No active temperature filter"
                break
            #Exit without changing anything
            elif r1 == "back":
                break
            
            r2 = inputLimit("Please enter an upper limit: ")
            #Break if clear
            if r2 == "clear":
                tempActive = "No active temperature filter"
                break
            #Exit without changing anything
            elif r2 == "back":
                break
                
            #Puts the values in the correct order
            tempActive = [min(r1,r2),max(r1,r2)]
            break
        
    #Bacteria filter
    elif filtertype == "Bacteria filter":
        header("BACTERIA FILTER MENU") #Interface
        print("""You have chosen to filter for bacteria.
Select the bacteria you want to see
If it is already a filter, it will be removed\n""")
                
        while True:
            printFilter(bacActive,growthActive,tempActive) #Print filter
            menu = int(displayMenu(bacStr+["Back"])) #Displays a menu
            
            #Back
            if menu == 5:
                break
            
            #Checks if bacteria chosen is in our bacList
            if menu in bacList:
                bacList = bacList[bacList != menu] #Remove from array
            else:
                bacList = np.append(bacList,menu) #Add to array
            
            bacActive = np.array(bacStr)[bacList-1] #Active bacteria filter
            
            if len(bacActive) == 0:
                bacActive = "No active bacteria filter" 

    #Use mask and range_ to filter data if filter is active (specific type)
    if type(bacActive) != str: #For bacteria
        mask = np.in1d(dataOld[:,2],bacList) #Where each value of bacList is in dataOld
        data = dataOld[mask] #Masking from unfiltered data
        
    else:
        data = dataOld #Data is the same as old
    
    if type(growthActive) != str: #For growth rate range
        range_ = ((growthActive[0] < data[:,1]) & (data[:,1] < growthActive[1]))   
        data = data[range_] #Data is filtered for growth rate range
        
    if type(tempActive) != str: #For temperature range
        range_ = ((tempActive[0] < data[:,0]) & (data[:,0] < tempActive[1]))   
        data = data[range_] #Data is filtered for temperature range
        
    if not (type(bacActive) != str) or (type(growthActive) != str) or (type(tempActive) != str):
        data = data #No changes to data, but it is pre-filtered
    
    #Contain conditions from filter function in list
    conditions = [bacActive,growthActive,tempActive,bacList,range_,mask]
    
    return data,conditions