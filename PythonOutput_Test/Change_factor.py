#This script was written by Warren Kunkler on 1/2/2017 in support of the Loca download project for Keely Brooks
#The output of this script is a csv file that contains the calculated change factor based off of the annual mean for each selected time period
#our baseline time period for the historical projection is 1971-2000 and the time period for the future projection is 2021-2050.
#For the temperature data it is calculated by finding the difference between the two time periods and for the precipitation data it is calculated by dividing the two time periods

import os

#These two variables need user input to point in the appropriate directories that house the annual stats
#for both projections
Historical_dir = raw_input("Enter a directory of the historical annual stats compiled: ")


Future_Dir = raw_input("Enter a directory of the future annual stats compiled: ")


#This function takes each input and calculates the final change factor output
def calculateChangeFactors(Historical_File, Future_File, filename, filename2):

    #initialize two sets of lists, one to store the data from the two different csv files and two to
    #perform calculations with the data from the csv files
    Historical_list = []
    Future_list = []

    Baseline_calc_list = []
    Future_calc_list = []
    
    #Read the two csv files and create a separate csv for where all our calculations are to go
    Historical_ReadFile = open(Historical_File, 'r')
    Future_ReadFile = open(Future_File, 'r')
    Change_factor_outputFile = open(subDir + '\\' + 'Change_factor_' + filename2[0:-4] + '.csv', 'w')
    Change_factor_outputFile.write('Years' + ',' + 'Change Factor\n')
    
    #loop through the historical projected annual average stats file and read its contents
    for i in Historical_ReadFile:
        Historical_list.append(i)

    #loop through the future projected annual average stats file and read contents
    for x in Future_ReadFile:
        Future_list.append(x)


    #This loop ierates through the historical list and adds the data to the baseline calculations list if the year is between 1971 and 2000
    for iterator in range(1, len(Historical_list)):
        if int(Historical_list[iterator][0:4]) >= 1971 and int(Historical_list[iterator][0:4]) <= 2000 and ',' not in Historical_list[iterator][5:18]:
            Baseline_calc_list.append(float(Historical_list[iterator][5:18]))
        elif int(Historical_list[iterator][0:4]) >= 1971 and int(Historical_list[iterator][0:4]) <= 2000 and ',' not in Historical_list[iterator][5:17]:
            Baseline_calc_list.append(float(Historical_list[iterator][5:17]))
        elif int(Historical_list[iterator][0:4]) >= 1971 and int(Historical_list[iterator][0:4]) <= 2000 and ',' not in Historical_list[iterator][5:16]:
            Baseline_calc_list.append(float(Historical_list[iterator][5:16]))
        elif int(Historical_list[iterator][0:4]) >= 1971 and int(Historical_list[iterator][0:4]) <= 2000 and ',' not in Historical_list[iterator][5:15]:
            Baseline_calc_list.append(float(Historical_list[iterator][5:15]))
        elif int(Historical_list[iterator][0:4]) >= 1971 and int(Historical_list[iterator][0:4]) <= 2000 and ',' not in Historical_list[iterator][5:8]:
            Baseline_calc_list.append(float(Historical_list[iterator][5:8]))

    #This loop iterates through the future list and adds the data to the future calculations list if the year is between 2021 and 2050
    for iterator in range(1, len(Future_list)):
        if int(Future_list[iterator][0:4]) >= 2035 and int(Future_list[iterator][0:4]) <= 2050 and ',' not in Future_list[iterator][5:18]:
            Future_calc_list.append(float(Future_list[iterator][5:18]))
        elif int(Future_list[iterator][0:4]) >= 2035 and int(Future_list[iterator][0:4]) <= 2050 and ',' not in Future_list[iterator][5:17]:
            Future_calc_list.append(float(Future_list[iterator][5:17]))
        elif int(Future_list[iterator][0:4]) >= 2035 and int(Future_list[iterator][0:4]) <= 2050 and ',' not in Future_list[iterator][5:16]:
            Future_calc_list.append(float(Future_list[iterator][5:16]))
        elif int(Future_list[iterator][0:4]) >= 2035 and int(Future_list[iterator][0:4]) <= 2050 and ',' not in Future_list[iterator][5:15]:
            Future_calc_list.append(float(Future_list[iterator][5:15]))
        elif int(Future_list[iterator][0:4]) >= 2035 and int(Future_list[iterator][0:4]) <= 2050 and ',' not in Future_list[iterator][5:8]:
            Future_calc_list.append(float(Future_list[iterator][5:8]))

    #Here we initialize a count variable to keep track of the lines that are outputted 
    
    historic_year = 1971
    future_year = 2021


#new stuff 2/1/2017
    future_sum = 0
    historical_sum = 0

    historical_year_count = 0
    future_year_count = 0
    
    for iterator in Baseline_calc_list:
        historical_sum += iterator
        historical_year_count += 1
    Historical_Sim_Average = historical_sum/historical_year_count
    
    
    for iterator in Future_calc_list:
        future_sum += iterator
        future_year_count += 1
    Future_Sim_Average = future_sum/future_year_count

    if 'pr' in filename:
        text = "(2035 to 2050)/(1971 to 2000) \n"
        line = Future_Sim_Average/Historical_Sim_Average
    elif 'pr' not in filename:
        text = "(2035 to 2050) - (1971 to 2000) \n"
        line = Future_Sim_Average - Historical_Sim_Average

    str_line = str(line)
    Change_factor_outputFile.write(text)
    Change_factor_outputFile.write(str_line)

    
    """
    #This loop runs through the future and historic baseline calculation lists and computes the change factor
    #it also determines how to compute the change factor based on whether it is temp or precipitation data that is being used for calculations
    for calc_iterator in range(len(Future_calc_list)):
        if '_pr_' in filename:
            line = float(Future_calc_list[calc_iterator])/float(Baseline_calc_list[calc_iterator])
            str_line = str(future_year) + '/' + str(historic_year) + ',' + str(line) + '\n'
            Change_factor_outputFile.write(str_line)
        elif '_pr_' not in filename:
            line = float(Future_calc_list[calc_iterator]) - float(Baseline_calc_list[calc_iterator])
            str_line = str(future_year) + '-' + str(historic_year) + ',' + str(line) + '\n'
            Change_factor_outputFile.write(str_line)
        
        historic_year += 1
        future_year += 1"""


        
    #Once complete we break out of the loop and close both the future and historic annual averages files
    #we also close the newly created Change factor csv file
    Historical_ReadFile.close()
    Future_ReadFile.close()
    Change_factor_outputFile.close()




#These loops down here initiate the os.walk through the directory housing the annual average stats files for the historic projections    
for root, dirs, files in os.walk(Historical_dir):
    for filename in files:
        #we designate a subdirectory variable used to assist in the creation of the subdirectory
        subDir = root + '\ChangeFactor'
        if filename[-4:] == '.csv':
            
            #Grab the file location for each historical annual stats file
            Historical = root + '\\' + filename

            #create the necessary subdirectory that will house each change factor file that will be created by executing this script
            if not os.path.exists(subDir):
                os.makedirs(subDir)
            
           
            #with in the same loop we created another walk this time through the directory that houses the future projections
            for root2, dirs2, files2 in os.walk(Future_Dir):
                for filename2 in files2:
                    #This conditional statement makes sure that the future projection file matches the historical file
                    #This makes sure that we are matching each model from both different projections against the correct ones.
                    if 'pr' not in filename and filename2[-4:] == '.csv' and filename[0:18] in filename2:

                        #This variable points to the location of the actual future projection annual stats file
                        Future = root2 + '\\' + filename2

                        #Keeps calling the calculateChangeFactors function by plugging in all the variables that are defined with
                        #each iteration of the loop
                        calculateChangeFactors(Historical, Future, filename, filename2)
                        
                        
                           
                
                    elif 'pr' in filename and filename2[-4:] == '.csv' and filename[0:11] in filename2:

                        #This variable points to the location of the actual future projection annual stats file
                        Future = root2 + '\\' + filename2

                        #Keeps calling the calculateChangeFactors function by plugging in all the variables that are defined with
                        #each iteration of the loop
                        calculateChangeFactors(Historical, Future, filename, filename2)
          
