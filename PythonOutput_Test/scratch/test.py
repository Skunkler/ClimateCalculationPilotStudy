import os
import math
from math import *


my_list = []
ReadFile = open('H:\Keely_PythonProject\Sites\historical\Site1\_tasmax_ACCESS1-0_r1i1_historical_MonthlyAverage.csv','r')
OutFile = open('H:\PythonOutput_Test\Test.csv', 'w')
annual_sum_list = []

for i in ReadFile:
    my_list.append(i)
answer = 0

for year in range(1950, 2006):
    count = 0
    annual_sum = 0
    for iterator in range(0, len(my_list)):
        year_text = my_list[iterator][0:4]
        month = my_list[iterator][5:7]
        data = my_list[iterator][10::1]
        

        if year == int(year_text) and count < 13:
            count +=1
            if ',' in month:
                single_digit_month = month[-2:-1]
                annual_sum += float(data)
                annual_average = annual_sum/12
                #print year, year_text, single_digit_month, data, count, annual_sum, annual_average
        
            elif ',' not in month:
                data_doubleMonth = my_list[iterator][11::1]
                annual_sum += float(data_doubleMonth)
                annual_average = annual_sum/12
                #print year, year_text, month, data_doubleMonth, count, annual_average
                year_and_average = str(year) +',' + str(annual_average) +  '\n'
    print year, count, annual_average
    OutFile.write(year_and_average)
    



        
       
            

OutFile.close()
ReadFile.close()
