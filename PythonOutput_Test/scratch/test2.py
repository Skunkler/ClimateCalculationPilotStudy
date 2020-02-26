import os
import math
from math import *


annualAverage_list = []
monthlyAverage_list = []


ReadFile = open('H:\PythonOutput_Test\Test.csv','r')
ReadFile2 = open('H:\Keely_PythonProject\Sites\historical\Site1\_tasmax_ACCESS1-0_r1i1_historical_MonthlyAverage.csv', 'r')
OutFile = open('H:\PythonOutput_Test\Test_round2.csv', 'w')
annual_sum_list = []


print "Year\tAnnual Average\tVariance\tStandard Deviation\t 95% low \t 95% high\n"

for i in ReadFile:
    annualAverage_list.append(i)


for x in ReadFile2:
    monthlyAverage_list.append(x)



for year in range(0, len(annualAverage_list)):
    AnnualAverageYear_text = annualAverage_list[year][0:4]
    AnnualAverageYear_data_text = annualAverage_list[year][5:]
    AnnualAverageYear_data = float(AnnualAverageYear_data_text)
    
    variance_num = 0
    count = 0
    for iterator in range(0, len(monthlyAverage_list)):
        MonthlyAverageYear_text = monthlyAverage_list[iterator][0:4]
        MonthlyAverage_monthText = monthlyAverage_list[iterator][5:7]
        MonthlyAverage_dataText = monthlyAverage_list[iterator][10:]
        if AnnualAverageYear_text == MonthlyAverageYear_text and ',' not in MonthlyAverage_dataText:
            count += 1
            MonthlyAverage_data = float(MonthlyAverage_dataText)
            variance_num += (MonthlyAverage_data - AnnualAverageYear_data)**2
            #print AnnualAverageYear_text, AnnualAverageYear_data, MonthlyAverageYear_text, MonthlyAverage_data, count
            
            
        elif AnnualAverageYear_text == MonthlyAverageYear_text and ',' in MonthlyAverage_dataText:
            count += 1
            MonthlyAverage_dataText = monthlyAverage_list[iterator][11:]
            MonthlyAverage_data = float(MonthlyAverage_dataText)
            variance_num += (MonthlyAverage_data - AnnualAverageYear_data)**2
            #print AnnualAverageYear_text, AnnualAverageYear_data, MonthlyAverageYear_text, MonthlyAverage_data, count
    print AnnualAverageYear_text, AnnualAverageYear_data, variance_num/11, math.sqrt(variance_num/11), AnnualAverageYear_data - (2*math.sqrt(variance_num/11)), AnnualAverageYear_data + (2*math.sqrt(variance_num/11)) 
         
        
       
            

OutFile.close()
ReadFile.close()
