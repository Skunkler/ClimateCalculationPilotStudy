#This script was written by Warren Kunkler on December 15, 2016 in support of the LOCA Climate Data download and processing project for Keely Brooks from the USGS Data Portal

import os


Input_directory = raw_input('Please enter a directory: ')

#This loop goes through the directory and finds each csv file
for root, dirs, files in os.walk(Input_directory):
    for filename in files:
        subDir = root + '\MonthlyAverage'
        if filename[:4] == 'Loca':

            #initialize a my_list list variable
            my_list = []
            #each ReadFile variable will point to a new csv file
            ReadFile = open(root + '\\' + filename, 'r')

            #this statement checks to see if subdirectory is has already been created and if not then it generates the subdirectory
            if not os.path.exists(subDir):
                os.makedirs(subDir)
            OutFile = open(subDir + '\\' + filename[16:37] + '_historical_MonthlyAverage.csv', 'w')


            if 'Historical' in filename:
                a = 1950
                b = 2006
            elif 'rcp' in filename:
                a = 2006
                b = 2101

            #this loop stores the contents of each csv in the my_list variable for later
            for i in ReadFile:
                my_list.append(i)
            answer = 0

            #This loop iterates through the years and months, in this case the loop is set for historical projections from 1950 to 2005
            #the nested for loop iterates through months 1-12
            for x in range(a, b):
                for p in range(1, 13):

                    #we initialize two variables, the count1 variable represents the days and the sumVar1 variable represents the summation of the data
                    count1 = 0
                    sumVar1 = 0

                    #our next nested loop iterates through the contents of the my_list and pulls out the data for the month, year, day, and data and converts each
                    #to the proper data type for calculation
                    for iterator in range(3, len(my_list)):    
                   
                        month = my_list[iterator][5:7]
                        month_type = int(month)

                        year = my_list[iterator][:4]
                        year_type = int(year)
    

                        data = my_list[iterator][21::1]
                        data_type = float(data)

                        day = my_list[iterator][8:10]
                        day_type = int(day)

                        #this condition checks to see if our year and month iterators match the year and months listed on each line of the data
                        if x == year_type and p == month_type:

                            #if the lines do match then we increment the summation variable data by the daily data and the count1 variable is incremented by 1
                            #our answer variable equals the monthly mean or the total sum of all daily data divided by the number of days in that month
                
                            sumVar1 += data_type
                            count1 += 1
                            answer = sumVar1/count1

                    #Our line variable outputs all the data properly to be written to our output variable
                    #our OutFile variable then writes our line to each output file
                    line = str(x) + ',' + str(p) + ',' + str(count1) + ',' + str(answer) + '\n'
                    OutFile.write(line)

        #after calculating our data and writing it to the appropriate output file we break out of the loops and wipe the my_list variable
        #and we close the ReadFile and OutFile variables
        del my_list[:]
        ReadFile.close()
        OutFile.close()
        
