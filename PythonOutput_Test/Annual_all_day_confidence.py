#This script was written by Warren Kunkler on December 15, 2016 in support of the project to download and processing of the LOCA climate data from the USGS Data Portal for Keely Brooks


import os
import math
from math import *


input_dir = raw_input('Please enter a directory: ')


#This is the z-score used to calculate the 95% confidence interval since we have a known standard deviation
z = 1.96


#loop through all the csv files in the directory
for root, dirs, files in os.walk(input_dir):
    for filename in files:
        subDir = root + '\AnnualAverage'
        if filename[:4] == 'Loca':
            

            #initialize an empty list to store the contents of each csv in it
            my_list = []
            #The ReadFile points to each csv
            ReadFile = open(root + '\\' + filename, 'r')

            #creates the subdirectory if it doesn't already exist
            if not os.path.exists(subDir):
                os.makedirs(subDir)
            if 'Historical' in filename:
                a = 1950
                b = 2006
                OutFile = open(subDir + '\\' + filename[16:-4] + '_Annual_AllStats_Average.csv', 'w')
            elif 'rcp' in filename:
                OutFile = open(subDir + '\\' + filename[11:-4] + '_Annual_AllStats_Average.csv', 'w')
                a = 2006
                b = 2101
            OutFile.write('Year' + ',' + 'Annual Mean' + ',' + '# of days' + ',' + 'Variance' + ',' + 'StDEV' + ',' + 'Lower Limit 95% confidence' + ',' + 'Upper Limit 95% confidence' + '\n')

            #intialize another list
            Annual_Average_list = []
            for i in ReadFile:
                my_list.append(i)
            answer = 0
            
            #start out iterating through the years of interest. In this case we are iterating through the future scenarios starting from 2006 up to but not including 2101
            for year_iterator in range(a, b):

                #intializing two variables. The Count1 represents the number of days in the year and the summation variable represents the summation of all the data for all
                #days in the year
                count1 = 0
                sumVar1 = 0
                #iterates through the months starting from the 1st month all the way through and including the 12th month
                for p in range(1, 13):
                    count_text =0
                    #iterates through the contents of the csv file starting on the 3rd line all the way until the end
                    for iterator in range(3, len(my_list)):

                        #iterates through the contents and picks out the text values for the month, year, day, and the data and
                        #converts them to the appropriate data types
                        month = my_list[iterator][5:7]
                        month_type = int(month)

                        year = my_list[iterator][:4]
                        year_type = int(year)
    

                        data = my_list[iterator][21::1]
                        data_type = float(data)

                        day = my_list[iterator][8:10]
                        day_type = int(day)


                        #this conditional checks to see if our iterator matches the year pulled from the line in the csv file
                        #if it does we increment our count by 1, our summation variable is incremented by the data per line
                        #our answer is equal to the summing of all the data divided by the count which represents the number of days
                        #in the year
                        if year_iterator == year_type:
                            count1 += 1
                            count_text += 1
                            sumVar1 += data_type
                            answer = sumVar1/count1
                            
                
                #After breaking out of the loop that iterates through each line of the csv we designate a Line1 variable equal to
                #the data for the annual mean that is all casted as a string data type and appended to our Annual_Average_list
                Line1 = str(year_iterator) + ',' + str(count_text) + ',' + str(answer)
                Annual_Average_list.append(Line1)

            #this loop iterates through the Annual_Average_list and converts each piece of data to the appropriate datatypes
            for i in range(0, len(Annual_Average_list)):
                list_year_text = Annual_Average_list[i][0:4]
                list_year_data = float(Annual_Average_list[i][9:])
                list_year_Daycount = int(Annual_Average_list[i][5:8])
                #intialize a variable to represent the variance
                Variance_num2 = 0

                #reiterate through each csv file and convert the necessary data to the appropriate types
                for iterator in range(0, len(my_list)):
                    ReadFile_yearText = my_list[iterator][0:4]
                    ReadFile_dataText = my_list[iterator][21:]
                    count2 = 0
                    #if the year from our annual list matches the year found in the file of the csv increment our day count by 1
                    #convert the data to a float type and set the variance variable equal to the numerator for calculating the variance
                    if list_year_text == ReadFile_yearText:
                        count2 += 1
                        ReadFile_data = float(ReadFile_dataText)
                        Variance_num2 += (ReadFile_data - list_year_data)**2
            
                #This Variance variable is actually equal to the variance of the data and from this we can get the standard deviation by taking the square root of the variance
                #from that we calculate the margin error and then calculate the upper and lower limits of our 95% confidence interval
                Variance = Variance_num2/(list_year_Daycount - 1)
                Standard_Deviation = math.sqrt(Variance)
                Margin_Error = Standard_Deviation/math.sqrt(list_year_Daycount)
                Lower_limit_confidence = list_year_data - (z * Margin_Error)
                Upper_limit_confidence = list_year_data + (z * Margin_Error)
                
                #This line variable formats our output to be written to the outfile
                line2 = list_year_text + ',' + str(list_year_data) + ',' + str(list_year_Daycount) + ',' + str(Variance) + ',' + str(Standard_Deviation) \
                + ',' + str(Lower_limit_confidence) + ',' + str(Upper_limit_confidence) + '\n' 


                #write each line to the outfile
                OutFile.write(line2)
        #after incrementing through the annual average list we break out of the loops and conditions to wipe the contents of my_list and Annual_Average_list
        #We also close each ReadFile and OutFile and then go back to the first loop that will iterate to the next csv file
        del my_list[:]
        del Annual_Average_list[:]
        ReadFile.close()
        OutFile.close()
        
