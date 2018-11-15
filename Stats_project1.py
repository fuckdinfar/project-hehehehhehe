#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 13:27:24 2018

@author: Thomas, Frederik
"""

import numpy as np
def dataStatistics(data, statistic):

    #Calculates mean Temperature
    if statistic == 'Mean temperature':
        result = np.mean(data[:,0])
   
    #Calculates mean Growth rate
    elif statistic == 'Mean growth rate':
        result = np.mean(data[:,1])
   
    #Calculates standard deviation of Temperature
    elif statistic == 'Std temperature':
        result = np.std(data[:,0])
   
    #Calculates standard deviation of Growth rate
    elif statistic == 'Std growth rate':
        result = np.std(data[:,1])
   
    #Calculates the total number of rows in the data
    elif statistic == 'Rows':
        result = np.size(data[:,0])
   
    #Calculates mean Growth rate when temp < 20 degrees
    elif statistic == 'Mean cold growth rate':
        GRsum = 0
        GRamount = 0
        for i in range(len(data[:,0])):
            if data[i,0] < 20:
                GRsum = GRsum + data[i,1]
                GRamount = GRamount + 1
            if GRamount > 0:
                result = GRsum/GRamount
            else :
                result = 'No temperature below 20 degrees'
    
    #Calculates mean Growth rate when temp > 50 degrees
    elif statistic == 'Mean hot growth rate':
        GRHsum = 0
        GRHamount = 0
        for i in range(len(data[:,0])):
            if data[i,0] > 50:
                GRHsum = GRHsum + data[i,1]
                GRHamount = GRHamount + 1
            if GRHamount > 0:
                result = GRHsum/GRHamount
            else :
                result = 'No temperature above 50 degrees'
                
    else:
        result = 'Invalid input, try again'
    
    return result



        
    
