import os

#ReadFile = open(r"H:\Keely_PythonTest_Output\Loca_late_Feature_tasmax_EC-EARTH_r2i1p1_rcp85.csv", 'r')
#OutFile = open(r"H:\Keely_PythonTest_Output\Loca_Test_log.txt", 'w')


#my_list = []
answer_list = []


for root, dirs, files in os.walk(r"H:\Keely_PythonProject\Sites\historical\Site1"):
    for filename in files:
        if filename[-31:-22:1] == 'ACCESS1-0':
            my_list = []
            ReadFile = open(root + '\\' + filename, 'r')
            
            for i in ReadFile:
                my_list.append(i)
            answer = 0


            count2 = 0
            for x in range(1950, 2005):
                count2 += 1
                for p in range(1, 13):
                    count1 = 0
                    sumVar1 = 0


                    for iterator in range(3, len(my_list)):
            
            
                        
                        month = my_list[iterator][5:7]
                        month_type = int(month)

                        year = my_list[iterator][:4]
                        year_type = int(year)
    

                        data = my_list[iterator][21::1]
                        data_type = float(data)

                        day = my_list[iterator][8:10]
                        day_type = int(day)
                        #print month_type, year_type, day_type, data_type
                
                        if x == year_type and p == month_type:
                
                            sumVar1 += data_type
                            count1 += 1
                            answer = sumVar1/count1
                        answer_list.append(answer)
                print count2
                

month_count = 0
for y in range(1950, 2005):
    for months in range(1,13):
        month_count += 1
        print str(y) + ' ' + str(months) + ' ' + str(answer_list[month_count])

