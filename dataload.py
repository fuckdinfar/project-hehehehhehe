import csv
import numpy as np

def dataLoad(filename):
    # This function is created to take the data from a given file and inputs it into a N*3 matrix. 
    #It will also check if the data fulfills the given conditions and will print an error message 
    # otherwise with the error and the line the error occurs in.
  
    
    
    data = [0,0,0] # Our initial values.
    read = True
    
    with open(filename, newline='') as inputfile:
        for line,row in enumerate(csv.reader(inputfile)):
            
            arr = np.array(row[0].split(" "), dtype=float) #Creating an array
            #Only read line if len of the array is 3
            if len(arr) == 3:                
                #Checking for errors in our file
                if ((10 >= arr[0]) or (arr[0] >= 60)): #Temperature
                    read = False #Do not read line
                    print("Error: Temperature too low or too high:",line+1,"Skipping")
                    
                if (arr[1]<0): #Growth rate
                    read = False #Skip the line
                    print("Error: Negative growth rate:",line+1,"Skipping")
                
                
                if ((0 >= arr[2]) or (arr[2] > 4)): #Bacteria
                    read = False #Skip the line
                    print("Error: Invalid bacteria type",line+1,'Skipping')
                
                if read:
                    data = np.vstack((data,arr)) #Stacks the data into an N*3 matrix
                
                read = True 
                
            else:
                print('Lenght of row not 3', line+1,'Skipping')
    
    data = data[1:len(data)] #Remove our data placeholder we creating in the beginning
    

    return data
print(dataLoad('test.txt'))