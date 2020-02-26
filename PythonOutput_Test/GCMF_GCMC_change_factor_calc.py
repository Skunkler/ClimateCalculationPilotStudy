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
    Change_factor_outputFile.write('months' + ',' + 'Change Factor\n')
    
    #loop through the historical projected annual average stats file and read its contents
    for i in Historical_ReadFile:
        Historical_list.append(i)

    #loop through the future projected annual average stats file and read contents
    for x in Future_ReadFile:
        Future_list.append(x)

    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    line5 = ""
    line6 = ""
    line7 = ""
    line8 = ""
    line9 = ""
    line10 = ""
    line11 = ""
    line12 = ""

    
    #This loop ierates through the historical list and adds the data to the baseline calculations list if the year is between 1971 and 2000
    if 'pr' in filename:
        print "divide"
        for iterator in range(1, len(Historical_list)):
            if Historical_list[iterator][:7] == "January" and Future_list[iterator][:7] == "January":
                Historical_var = float(Historical_list[iterator][8:])
                Future_var = float(Future_list[iterator][8:])
                answer = Future_var/Historical_var
                line1 = "January," + str(answer) + '\n'
                Change_factor_outputFile.write(line1)
                
                
            elif Historical_list[iterator][:8] == "February" and Future_list[iterator][:8] == "February":
                Historical_var = float(Historical_list[iterator][9:])
                Future_var = float(Future_list[iterator][9:])
                answer = Future_var/Historical_var
                line2 = "February," + str(answer) + '\n'
                Change_factor_outputFile.write(line2)

                
            elif Historical_list[iterator][:5] == "March" and Future_list[iterator][:5] == "March":
                Historical_var = float(Historical_list[iterator][6:])
                Future_var = float(Future_list[iterator][6:])
                answer = Future_var/Historical_var
                line3 = "March," + str(answer) + '\n'
                Change_factor_outputFile.write(line3)

                
            elif Historical_list[iterator][:5] == "April" and Future_list[iterator][:5] == "April":
                Historical_var = float(Historical_list[iterator][6:])
                Future_var = float(Future_list[iterator][6:])
                answer = Future_var/Historical_var
                line4 = "April," + str(answer) + '\n'
                Change_factor_outputFile.write(line4)

                
            elif Historical_list[iterator][:3] == "May" and Future_list[iterator][:3] == "May":
                Historical_var = float(Historical_list[iterator][4:])
                Future_var = float(Future_list[iterator][4:])
                answer = Future_var/Historical_var
                line5 = "May," + str(answer) + '\n'
                Change_factor_outputFile.write(line5)
                
            
            elif Historical_list[iterator][:4] == "June" and Future_list[iterator][:4] == "June":
                Historical_var = float(Historical_list[iterator][5:])
                Future_var = float(Future_list[iterator][5:])
                answer = Future_var/Historical_var
                line6 = "June," + str(answer) + '\n'
                Change_factor_outputFile.write(line6)
            
            
            elif Historical_list[iterator][:4] == "July" and Future_list[iterator][:4] == "July":
                Historical_var = float(Historical_list[iterator][5:])
                Future_var = float(Future_list[iterator][5:])
                answer = Future_var/Historical_var
                line7 = "July," + str(answer) + '\n'
                Change_factor_outputFile.write(line7)

                
            elif Historical_list[iterator][:6] == "August" and Future_list[iterator][:6] == "August":
                Historical_var = float(Historical_list[iterator][7:])
                Future_var = float(Future_list[iterator][7:])
                answer = Future_var/Historical_var
                line8 = "August," + str(answer) + '\n'
                Change_factor_outputFile.write(line8)
                
            
            elif Historical_list[iterator][:9] == "September" and Future_list[iterator][:9] == "September":
                Historical_var = float(Historical_list[iterator][10:])
                Future_var = float(Future_list[iterator][10:])
                answer = Future_var/Historical_var
                line9 = "September," + str(answer) + '\n'
                Change_factor_outputFile.write(line9)
                
            
            elif Historical_list[iterator][:7] == "October" and Future_list[iterator][:7] == "October":
                Historical_var = float(Historical_list[iterator][8:])
                Future_var = float(Future_list[iterator][8:])
                answer = Future_var/Historical_var
                line10 = "October," + str(answer) + '\n'
                Change_factor_outputFile.write(line10)
                
            
            elif Historical_list[iterator][:8] == "November" and Future_list[iterator][:8] == "November":
                Historical_var = float(Historical_list[iterator][9:])
                Future_var = float(Future_list[iterator][9:])
                answer = Future_var/Historical_var
                line11 = "November," + str(answer) + '\n'
                Change_factor_outputFile.write(line11)

                
            elif Historical_list[iterator][:8] == "December" and Future_list[iterator][:8] == "December":
                Historical_var = float(Historical_list[iterator][9:])
                Future_var = float(Future_list[iterator][9:])
                answer = Future_var/Historical_var
                line12 = "December," + str(answer) + '\n'
                Change_factor_outputFile.write(line12)

                

    elif 'pr' not in filename:
        print "subtract"
        for iterator in range(1, len(Historical_list)):
            if Historical_list[iterator][:7] == "January" and Future_list[iterator][:7] == "January":
                Historical_var = float(Historical_list[iterator][8:])
                Future_var = float(Future_list[iterator][8:])
                answer = Future_var - Historical_var
                line1 = "January," + str(answer) + '\n'
                Change_factor_outputFile.write(line1)

                
            elif Historical_list[iterator][:8] == "February" and Future_list[iterator][:8] == "February":
                Historical_var = float(Historical_list[iterator][9:])
                Future_var = float(Future_list[iterator][9:])
                answer = Future_var - Historical_var
                line2 = "February," + str(answer) + '\n'
                Change_factor_outputFile.write(line2)

                
            elif Historical_list[iterator][:5] == "March" and Future_list[iterator][:5] == "March":
                Historical_var = float(Historical_list[iterator][6:])
                Future_var = float(Future_list[iterator][6:])
                answer = Future_var - Historical_var
                line3 = "March," + str(answer) + '\n'
                Change_factor_outputFile.write(line3)

                
            elif Historical_list[iterator][:5] == "April" and Future_list[iterator][:5] == "April":
                Historical_var = float(Historical_list[iterator][6:])
                Future_var = float(Future_list[iterator][6:])
                answer = Future_var - Historical_var
                line4 = "April," + str(answer) + '\n'
                Change_factor_outputFile.write(line4)

                
            elif Historical_list[iterator][:3] == "May" and Future_list[iterator][:3] == "May":
                Historical_var = float(Historical_list[iterator][4:])
                Future_var = float(Future_list[iterator][4:])
                answer = Future_var - Historical_var
                line5 = "May," + str(answer) + '\n'
                Change_factor_outputFile.write(line5)
                
            
            elif Historical_list[iterator][:4] == "June" and Future_list[iterator][:4] == "June":
                Historical_var = float(Historical_list[iterator][5:])
                Future_var = float(Future_list[iterator][5:])
                answer = Future_var - Historical_var
                line6 = "June," + str(answer) + '\n'
                Change_factor_outputFile.write(line6)
                
            
            elif Historical_list[iterator][:4] == "July" and Future_list[iterator][:4] == "July":
                Historical_var = float(Historical_list[iterator][5:])
                Future_var = float(Future_list[iterator][5:])
                answer = Future_var - Historical_var
                line7 = "July," + str(answer) + '\n'
                Change_factor_outputFile.write(line7)
                
                
            elif Historical_list[iterator][:6] == "August" and Future_list[iterator][:6] == "August":
                Historical_var = float(Historical_list[iterator][7:])
                Future_var = float(Future_list[iterator][7:])
                answer = Future_var - Historical_var
                line8 = "August," + str(answer) + '\n'
                Change_factor_outputFile.write(line8)
                
            
            elif Historical_list[iterator][:9] == "September" and Future_list[iterator][:9] == "September":
                Historical_var = float(Historical_list[iterator][10:])
                Future_var = float(Future_list[iterator][10:])
                answer = Future_var - Historical_var
                line9 = "September," + str(answer) + '\n'
                Change_factor_outputFile.write(line9)
                
            
            elif Historical_list[iterator][:7] == "October" and Future_list[iterator][:7] == "October":
                Historical_var = float(Historical_list[iterator][8:])
                Future_var = float(Future_list[iterator][8:])
                answer = Future_var - Historical_var
                line10 = "October," + str(answer) + '\n'
                Change_factor_outputFile.write(line10)
                
            
            elif Historical_list[iterator][:8] == "November" and Future_list[iterator][:8] == "November":
                Historical_var = float(Historical_list[iterator][9:])
                Future_var = float(Future_list[iterator][9:])
                answer = Future_var - Historical_var
                line11 = "November," + str(answer) + '\n'
                Change_factor_outputFile.write(line11)
                
                
            elif Historical_list[iterator][:8] == "December" and Future_list[iterator][:8] == "December":
                Historical_var = float(Historical_list[iterator][9:])
                Future_var = float(Future_list[iterator][9:])
                answer = Future_var - Historical_var
                line12 = "December," + str(answer) + '\n'
                Change_factor_outputFile.write(line12)

        
    #Once complete we break out of the loop and close both the future and historic annual averages files
    #we also close the newly created Change factor csv file
    Historical_ReadFile.close()
    Future_ReadFile.close()
    Change_factor_outputFile.close()




#These loops down here initiate the os.walk through the directory housing the annual average stats files for the historic projections    
for root, dirs, files in os.walk(Historical_dir):
    for filename in files:
        #we designate a subdirectory variable used to assist in the creation of the subdirectory
        subDir = root + '\ChangeFactor2'
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
          

