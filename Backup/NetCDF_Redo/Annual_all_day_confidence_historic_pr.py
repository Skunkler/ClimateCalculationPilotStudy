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
        if filename[-4::1] == '.csv' and 'GCMF' not in root and 'pr' in filename and 'AnnualAverage' not in root:
            print filename
        
            ReadFile = open(root + '\\' + filename, 'r')

            #creates the subdirectory if it doesn't already exist
            if not os.path.exists(subDir):
                os.makedirs(subDir)
            
            OutFile = open(subDir + '\\' + filename[:-4] + '_Annual_AllStats_Average.csv', 'w')
            OutFile.write('Year' + ',' + 'Annual Mean' + ',' + '# of days' + ',' + 'Variance' + ',' + 'StDEV' + ',' + 'Lower Limit 95% confidence' + ',' + 'Upper Limit 95% confidence' + '\n')
            
            
            lines = ReadFile.readlines()
            lines2 = ReadFile.readlines()
            Annual_Average_list = []
            for year_iterator in range(1950, 2006):
                count1 = 1
                sumVar1=0
                for i in lines:
                    if i.split(',')[0] != 'time':
                    
                    
                        month = i.split(',')[0].split('/')[0]
                        day = i.split(',')[0].split('/')[1]
                        year = i.split(',')[0].split('/')[2][:4]
                        data = i.split(',')[1]
                        #print month, day, year, data
                        if year_iterator == int(year):
                        
                            sumVar1 += float(data)
                            #answer = sumVar1/count1
                            count1 += 1
                if count1 == 1:
                    answer = sumVar1
                elif count1 > 1:
                    answer = sumVar1/(count1-1)
                Line1 = year_iterator, count1, answer
                #print Line1, answer
                Annual_Average_list.append(Line1)
            
        
            for i in range(0, len(Annual_Average_list)):
                Year_calc = Annual_Average_list[i][0]
                day_Count = Annual_Average_list[i][1]
                list_data = Annual_Average_list[i][2]
                Variance_num2 = 0
        
                for iterator in lines:
                    if iterator.split(',')[0] != 'time':

                        month = iterator.split(',')[0].split('/')[0]
                        day = iterator.split(',')[0].split('/')[1]
                        year = iterator.split(',')[0].split('/')[2][:4]
                        data = iterator.split(',')[1]

                    if int(year) == Year_calc:
                        Variance_num2 += (float(data) - list_data)**2
                        Variance = Variance_num2/(day_Count - 1)
                        Standard_Deviation = math.sqrt(Variance)
                        Margin_Error = Standard_Deviation/math.sqrt(day_Count)
                        Lower_limit_confidence = (list_data * day_Count) - (z * Margin_Error)
                        Upper_limit_confidence = (list_data * day_Count) + (z * Margin_Error)

                        
                line2 = str(Year_calc) + ',' + str(list_data * day_Count) + ',' + str(day_Count-1) + ',' + str(Variance) + ',' + str(Standard_Deviation) + ',' + \
                            str(Lower_limit_confidence) + ',' + str(Upper_limit_confidence) + '\n'
                #print line2
                OutFile.write(line2)

    OutFile.close()
    ReadFile.close()
                    
                
            
            
                  
                    
                
            #OutFile.close()
        
