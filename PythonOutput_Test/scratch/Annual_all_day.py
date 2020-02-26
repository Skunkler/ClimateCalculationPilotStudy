import os
import math
from math import *


for root, dirs, files in os.walk(r"H:\Keely_PythonProject\Sites\historical\Kyle_Canyon"):
    for filename in files:
        subDir = root + '\AnnualAverage2'
        if filename[:4] == 'Loca':
            
            my_list = []
            ReadFile = open(root + '\\' + filename, 'r')
            if not os.path.exists(subDir):
                os.makedirs(subDir)
            OutFile = open(subDir + '\\' + filename[16:37] + '_historical_Annual_AllStats_Average.csv', 'w')
            OutFile.write('Year' + ',' + 'Annual Mean' + ',' + '# of days' + ',' + 'Variance' + ',' + 'StDEV' + ',' + 'Annual mean - 2 StDev' + ',' + 'Annual Mean + 2 StDev' + '\n')

            Annual_Average_list = []
            for i in ReadFile:
                my_list.append(i)
            answer = 0

            for year_iterator in range(1950, 2006):
                count1 = 0
                sumVar1 = 0
                for p in range(1, 13):
                    count_text =0
                    for iterator in range(3, len(my_list)):
                   
                        month = my_list[iterator][5:7]
                        month_type = int(month)

                        year = my_list[iterator][:4]
                        year_type = int(year)
    

                        data = my_list[iterator][21::1]
                        data_type = float(data)

                        day = my_list[iterator][8:10]
                        day_type = int(day)
                       
                        if year_iterator == year_type:
                            count1 += 1
                            count_text += 1
                            sumVar1 += data_type
                            answer = sumVar1/count1
                            
                #print filename, year_iterator, count_text, answer
                Line1 = str(year_iterator) + ',' + str(count_text) + ',' + str(answer)
                Annual_Average_list.append(Line1)

            for i in range(0, len(Annual_Average_list)):
                list_year_text = Annual_Average_list[i][0:4]
                list_year_data = float(Annual_Average_list[i][9:])
                list_year_Daycount = int(Annual_Average_list[i][5:8])
                Variance_num2 = 0
                #print filename, list_year_text, list_year_Daycount, list_year_data
                for iterator in range(0, len(my_list)):
                    ReadFile_yearText = my_list[iterator][0:4]
                    ReadFile_dataText = my_list[iterator][21:]
                    count2 = 0
                    if list_year_text == ReadFile_yearText:
                        count2 += 1
                        ReadFile_data = float(ReadFile_dataText)
                        Variance_num2 += (ReadFile_data - list_year_data)**2
                #print filename, list_year_text, list_year_Daycount, ReadFile_data, Variance_num2/(list_year_Daycount - 1), math.sqrt(Variance_num2/(list_year_Daycount - 1))

                line2 = list_year_text + ',' + str(list_year_data) + ',' + str(list_year_Daycount) + ',' + str(Variance_num2/(list_year_Daycount - 1)) + ',' + str(math.sqrt(Variance_num2/(list_year_Daycount - 1))) \
                + ',' + str(list_year_data - (2*math.sqrt(Variance_num2/(list_year_Daycount - 1)))) + ',' + str(list_year_data + (2*math.sqrt(Variance_num2/(list_year_Daycount - 1)))) + '\n' 



                OutFile.write(line2)
        del my_list[:]
        del Annual_Average_list[:]
        ReadFile.close()
        OutFile.close()
        
