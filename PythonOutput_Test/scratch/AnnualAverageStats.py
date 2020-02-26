import os
import math
from math import *

for root, dirs, files in os.walk(r"H:\Keely_PythonProject\Sites\historical\Site1\MonthlyAverage"):
    for filename in files:
        subDir = root + '\AnnualAverage'
        if 'MonthlyAverage' in filename :


            if not os.path.exists(subDir):
                os.makedirs(subDir)

            OutFile = open(subDir + '\\' + filename[:21] + '_historical_Annual_Stats.csv', 'w')
            ReadFile_list = []
            ReadFile = open(root + '\\' + filename,'r')
            OutFile.write('Year' + ',' + 'Months' + ',' + 'Annual Average' + ',' + 'Variance' + ',' + 'Standard Deviation' + ',' + 'Mean minus 2 STDEV' + ',' + 'Mean plus 2 STDEV\n')
            annual_sum_list = []

            for i in ReadFile:
                ReadFile_list.append(i)
            answer = 0

            for year in range(1950, 2006):
                count = 0
                annual_sum = 0
                annual_average = 0
                for iterator in range(0, len(ReadFile_list)):
                    year_text = ReadFile_list[iterator][0:4]
                    month = ReadFile_list[iterator][5:7]
                    data = ReadFile_list[iterator][10:]
        

                    if year == int(year_text):
                        count +=1
                        if ',' in month:
                            single_digit_month = month[-2:-1]
                            annual_sum += float(data)
                        elif ',' not in month:
                            data_doubleMonth = ReadFile_list[iterator][11:]
                            annual_sum += float(data_doubleMonth)
                            annual_average = annual_sum/12
                        
                
                            year_and_average = filename+ ', ' + str(year) + ', ' + str(annual_average)
                #print filename, year, count, annual_average
                annual_sum_list.append(year_and_average)
            for i in range(0, len(annual_sum_list)):
                list_year_text = annual_sum_list[i][53:57]
                list_year_data = float(annual_sum_list[i][58:])
                list_year_model=annual_sum_list[i][0:51]
                Variance_num2 = 0
                count2 = 0
                #print list_year_model, list_year_text, list_year_data
                for iterator in range(0, len(ReadFile_list)):
                    ReadFile_yearText = ReadFile_list[iterator][0:4]
                    ReadFile_monthText = ReadFile_list[iterator][5:7]
                    ReadFile_dataText = ReadFile_list[iterator][10:]
                    if list_year_text == ReadFile_yearText and ',' not in ReadFile_dataText:
                        count2 += 1
                        Monthly_Average_Data = float(ReadFile_dataText)
                        Variance_num2 += (Monthly_Average_Data - list_year_data)**2

                    elif list_year_text == ReadFile_yearText and ',' in ReadFile_dataText:
                        count2 += 1
                        ReadFile_dataText = ReadFile_list[iterator][11:]
                        Monthly_Average_Data = float(ReadFile_dataText)
                        Variance_num2 += (Monthly_Average_Data - list_year_data)**2
                #print filename, list_year_data, Variance_num2/11, math.sqrt(Variance_num2/11), list_year_data - (2*math.sqrt(Variance_num2/11)), list_year_data + (2*math.sqrt(Variance_num2/11)), count2, list_year_text
                line2 = list_year_text + ',' + str(count2) + ',' + str(list_year_data) + ',' + str(Variance_num2/11) + ',' + str(math.sqrt(Variance_num2/11)) + ',' + str(list_year_data - (2*math.sqrt(Variance_num2/11))) + ',' + str(list_year_data + (2*math.sqrt(Variance_num2/11))) + '\n'
                OutFile.write(line2)
                
                                                                                                                                                                    
            annual_sum_list[:]
    
    



        
       
            

OutFile.close()
ReadFile.close()
