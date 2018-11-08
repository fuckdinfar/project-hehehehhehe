#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 15:39:05 2018

@author: Thomas
"""

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
def dataPlot(data):
    
    #Number of bacteria
    
    #Lists the names of the different bacteria
    objects = ('Salmonella enterica', 'Bacillus cereus', 'Listeria', 'Brochothrix thermosphacta')
    x_pos = np.arange(len(objects))
    
    #This section extracts the number of times each bacteria is represented in the data
    ones = data[:,2] == 1
    ones = np.extract(ones,data[:,2])
    A = np.size(ones)
    
    twos = data[:,2] == 2
    twos = np.extract(twos,data[:,2])
    B = np.size(twos)
    
    threes = data[:,2] == 3
    threes = np.extract(threes,data[:,2])
    C = np.size(threes)
    
    fours = data[:,2] == 4
    fours = np.extract(fours,data[:,2])
    D = np.size(fours)
    
    amount = [A,B,C,D]
    
    #Plots the data
    plt.bar(x_pos, amount, align='center', alpha=1, color=['salmon', 'fuchsia', 'springgreen', 'dodgerblue'], width = 0.7, edgecolor = "k")
    plt.xticks(x_pos, objects, rotation = 20)
    plt.title('Number of bacteria')
    plt.xlabel('Bacteria', fontsize = 5)
    plt.ylabel('Amount', fontsize = 10)
    plt.show()
    
    
    #Growth rate by temperature

    
    dataBac = data[data[:,2] == 1]
    if len(data > 0):
        #Sorts data after temperatures in ascending order
        sortedTemp = dataBac[dataBac[:,0].argsort()]
        x1 = sortedTemp[:,0]
        y1 = sortedTemp[:,1]
        
        #Plots the data
        plt.plot(x1,y1, color = 'salmon', linewidth = 2.5, label = objects[0])
        plt.legend()        
                
    dataBac = data[data[:,2] == 2]
    if len(data > 0):
        #Sorts data after temperatures in ascending order
        sortedTemp = dataBac[dataBac[:,0].argsort()]
        x2 = sortedTemp[:,0]
        y2 = sortedTemp[:,1]
        
        #Plots the data
        plt.plot(x2,y2, color = 'fuchsia', linewidth = 2.5, label = objects[1])
        plt.legend()
              
    dataBac = data[data[:,2] == 3]
    if len(data > 0):
        #Sorts data after temperatures in ascending order
        sortedTemp = dataBac[dataBac[:,0].argsort()]
        x3 = sortedTemp[:,0]
        y3 = sortedTemp[:,1]
        
        #Plots the data
        plt.plot(x3,y3, color = 'springgreen', linewidth = 2.5, label = objects[2])
        plt.legend()
               
    dataBac = data[data[:,2] == 4]
    if len(data > 0):
        #Sorts data after temperatures in ascending order
        sortedTemp = dataBac[dataBac[:,0].argsort()]
        x4 = sortedTemp[:,0]
        y4 = sortedTemp[:,1]
        
        #Plots the data
        plt.plot(x4,y4, color = 'dodgerblue', linewidth = 2.5, label = objects[3])
        plt.legend()
        
        
    plt.xlim([10,60])
    plt.ylim(ymin = 0)
    plt.title("Growth rate by temperature")
    plt.xlabel("Temperature", fontsize = 10)
    plt.ylabel("Growth rate", fontsize = 10)
    plt.show()
    
    

data = dataLoad('test.txt')
print(dataPlot(data))




