import os


#my_list = []

input_directory = raw_input('Please enter a directory: ')

for root, dirs, files in os.walk(input_directory):
    for filename in files:
        subdir = root + '\GCMF_GCMC2'
        if filename[:4] == 'Loca':
            my_list = []
            ReadFile = open(root + '\\' + filename, 'r')
            

            if not os.path.exists(subdir):
                os.makedirs(subdir)

            if 'Historical' in filename:
                a = 1971
                b = 2000
                OutFile = open( subdir + '\\' + filename[16:-4] + '_GCMF_GCMC_Averages.csv', 'w')
            elif 'rcp' in filename:
                a = 2051
                b = 2070
                OutFile = open( subdir + '\\' + filename[11:-4] + '_GCMF_GCMC_Averages.csv', 'w')

            OutFile.write('Month' + ',' 'Value\n')
            
            for i in ReadFile:
                my_list.append(i)
            answer = 0

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
            

        
            count1 = 0
            count2 = 0 
            count3 = 0
            count4 = 0
            count5 = 0
            count6 = 0
            count7 = 0
            count8 = 0
            count9 = 0
            count10 = 0
            count11 = 0
            count12 = 0
            ans12 = 0
            for iterator in range(3, len(my_list)):    
               
                month = my_list[iterator][5:7]
                month_type = int(month)
            
                year = my_list[iterator][:4]
                year_type = int(year)
    

                data = my_list[iterator][21::1]
                data_type = float(data)

                day = my_list[iterator][8:10]
                day_type = int(day)
                if year_type >= a and year_type <= b:
                    #print year_type
                    if int(month) == 1:
                        Jan += float(data)
                        count1 += 1
                        ans1 = Jan/count1
                    
                                
                    elif int(month) == 2:
                        Feb += float(data)
                        count2 += 1
                        ans2 = Feb/count2
                                
                    elif int(month) == 3:
                        Mar += float(data)
                        count3 += 1
                        ans3 = Mar/count3
                                
                    elif int(month) == 4:
                        Apr += float(data)
                        count4 += 1
                        ans4 = Apr/count4
                                
                    elif int(month) == 5:
                        May += float(data)
                        count5 += 1
                        ans5 = May/count5
                                
                    elif int(month) == 6:
                        June += float(data)
                        count6 += 1
                        ans6 = June/count6
                                
                    elif int(month) == 7:
                        July+= float(data)
                        count7 += 1
                        ans7 = July/count7
                                
                    elif int(month) == 8:
                        Aug += float(data)
                        count8 += 1
                        ans8 = Aug/count8
                                
                    elif int(month) == 9:
                        Sept += float(data)
                        count9 += 1
                        ans9 = Sept/count9
                                
                    elif int(month) == 10:
                        Oct += float(data)
                        count10 += 1
                        ans10 = Oct/count10
                                
                    elif int(month) == 11:
                        Nov += float(data)
                        count11 += 1
                        ans11 = Nov/count11
                                
                    elif int(month) == 12:
                        Dec += float(data)
                        count12 += 1
                        ans12 = Dec/count12
                              

            OutFile.write('January' + ',' + str(ans1) + '\n')
            OutFile.write('February' + ',' + str(ans2) + '\n')
            OutFile.write('March' + ',' + str(ans3) + '\n')
            OutFile.write('April' + ',' + str(ans4) + '\n')
            OutFile.write('May' + ',' + str(ans5) + '\n')
            OutFile.write('June' + ',' + str(ans6) + '\n')
            OutFile.write('July' + ',' + str(ans7) + '\n')
            OutFile.write('August' + ',' + str(ans8) + '\n')
            OutFile.write('September' + ',' + str(ans9) + '\n')
            OutFile.write('October' + ',' + str(ans10) + '\n')
            OutFile.write('November' + ',' + str(ans11) + '\n')
            OutFile.write('December' + ',' + str(ans12) + '\n')
    del my_list[:]
    ReadFile.close()
    OutFile.close()
        
