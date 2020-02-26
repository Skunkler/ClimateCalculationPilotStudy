#This script was created on 12/26/2016 by Warren Kunkler in support of the Loca Climate Data Downloading and processing project for Keely Brooks

import os

#This loop iterates through the directory and locates all the csv files we want to use for our calculations
for root, dirs, files in os.walk(r"H:\Keely_PythonProject\Sites\historical\BlueDiamond_RedRock_pr\MonthlyAverage"):
    for filename in files:
        if filename[-4:] == '.csv':


            #we initialize an empty my_list variable and set the ReadFile variable to each csv in the directory
            my_list = []
            ReadFile = open(root + '\\' + filename, 'r')


            #here we loop through the contents of each csv and append them to the my_list variable
            for i in ReadFile:
                my_list.append(i)

            #initialize a bunch of variables representing the months of the year
            Jan = 0
            Feb = 0
            Mar = 0
            Apr = 0
            May = 0
            June = 0
            July = 0
            Aug = 0
            Sept = 0
            Oct = 0
            Nov = 0
            Dec = 0

            #here we iterate through the contents of each csv file by iterating through the my_list variable
            for iterator in range(0, len(my_list)):

                #We grab each variable representing the month, year, and day   
                month = my_list[iterator][5:7]
                year = my_list[iterator][:4]
                days = my_list[iterator][8:10]
                        
                #here we calculate whether or not there is still a comma in our month variable and if so we adjust our variable to remove the commas
                if ',' in month:
                    month = my_list[iterator][5:6]
                    data = my_list[iterator][10:]
                    days = my_list[iterator][7:9]
                #if there is no comma in the month variable we keep it as is and just adjust the data variable
                elif ',' not in month:
                    month = month
                    days = days
                    data = my_list[iterator][11:]
                
                #here we select for each month and increment each month variable by the amount of the data for that month
                if int(month) == 1:
                    Jan += float(data)
                elif int(month) == 2:
                    Feb += float(data)
                elif int(month) == 3:
                    Mar += float(data)
                elif int(month) == 4:
                    Apr += float(data)
                elif int(month) == 5:
                    May += float(data)
                elif int(month) == 6:
                    June += float(data)
                elif int(month) == 7:
                    July+= float(data)
                elif int(month) == 8:
                    Aug += float(data)
                elif int(month) == 9:
                    Sept += float(data)
                elif int(month) == 10:
                    Oct += float(data)
                elif int(month) == 11:
                    Nov += float(data)
                elif int(month) == 12:
                    Dec += float(data)
                    
            print filename, Jan, Feb, Mar, Apr, May, June, July, Aug, Sept, Oct, Nov, Dec
                
                    
del my_list[:]
ReadFile.close()
#OutFile.close()
