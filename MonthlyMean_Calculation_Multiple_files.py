import os


#my_list = []



for root, dirs, files in os.walk(r"H:\Keely_PythonProject\Sites\historical\Site1"):
    for filename in files:
        if filename[-4::1] == '.csv':
            my_list = []
            ReadFile = open(root + '\\' + filename, 'r')
            OutFile = open(root + '\\' + filename[16:37] + '_historical_MonthlyAverage.csv', 'w')


            for i in ReadFile:
                my_list.append(i)
            answer = 0

            for x in range(1950, 2006):
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
                
                        if x == year_type and p == month_type:
                
                            sumVar1 += data_type
                            count1 += 1
                            answer = sumVar1/count1
                    line = str(x) + ',' + str(p) + ',' + str(count1) + ',' + str(answer) + '\n'
                    OutFile.write(line)
                    #print filename, x, p, count1, answer
        del my_list[:]
        ReadFile.close()
        OutFile.close()
        
