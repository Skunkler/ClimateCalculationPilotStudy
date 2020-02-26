import os

ReadFile = open(r"H:\Keely_PythonProject\Early\Loca_early_Future_pr_bcc-csm1-1-m_r1i1p1_rcp85.csv", 'r')
OutFile = open(r"H:\Keely_PythonTest_Output\Loca_Test.txt", 'w')


#my_list = []
answer_list = []



my_list = []

            
for i in ReadFile:
    my_list.append(i)
answer = 0
answer2 = 0
answer3 = 0
check_list = []

for x in range(2006, 2010):
    for p in range(1, 13):
        count1 = 0
        sumVar1 = 0
        ans1 = 0
        ans2 = 0
        ans3 = 0
        ans4 = 0
        answer3 = 0

        for i in range(3, len(my_list)):
            
            
            
            month = my_list[i][5:7]
            month_type = int(month)

            year = my_list[i][:4]
            year_type = int(year)
    

            data = my_list[i][21:33]
            #data_type = float(data)

            day = my_list[i][8:10]
            day_type = int(day)
            
            if 'E' in data:
                data2 = my_list[i][21:29]
                ref_data2 = my_list[i][21:29]
                if 'E' in data2:
                    data3 = my_list[i][21:28]
                    data3_type = float(data3)
                    data_exp = float(data[-3:])
                    ans1 = data3_type * (10**data_exp)
                    if x == year_type and p == month_type:
                
                        sumVar1 += ans1
                        count1 += 1
                        answer = sumVar1/count1
                        #print str(x) + " " + str(month_type) + " " + str(answer) + " " + str(count1)
                        final_answer = str(x) + " " + str(month_type) + " " + str(answer) + " " + day + '\n'
                        print final_answer
                        answer_list.append(final_answer)    
                        #OutFile.write(final_answer)


                    
                elif 'E' not in data2:
                    data2_type = float(data2)
                    data_exp2 = float(data[-2::])
                    if data_exp2 > 0:
                        data_exp2 = data_exp2 - (2 * data_exp2)
                        
                        if x == year_type and p == month_type:
                            ans2 = data2_type * (10**data_exp2)
                            sumVar1 += ans2
                            count1 += 1
                            ans2 = sumVar1/count1
                            #print str(x) + " " + str(month_type) + " " + str(ans2) + " " + str(count1)
                            final_answer = str(x) + " " + str(month_type) + " " + str(ans2) + " " + day +'\n'
                            print final_answer
                            answer_list.append(final_answer)
                            #OutFile.write(final_answer)
                        
                    else:# data_exp2 < 0:
                        if x == year_type and p == month_type:
                            ans3 = data2_type * (10**data_exp2)
                            sumVar1 += ans2
                            count1 += 1
                            ans3 = sumVar1/count1    
                            #print str(x) + " " + str(month_type) + " " + str(ans2) + " " + str(count1)
                            final_answer3 = str(x) + " " + str(month_type) + " " + str(ans2) + " " + day +'\n'
                            print final_answer3
                            answer_list.append(final_answer3)
                            #OutFile.write(final_answer)


                
            else:
                data_type = float(data)
    
                
                if x == year_type and p == month_type:
                
                    sumVar1 += data_type
                    count1 += 1
                    answer3 = sumVar1/count1
                    final_answer = str(x) + " " + str(month_type) + " " + str(answer3) + " " + day +'\n'
                    print final_answer
                    answer_list.append(final_answer)
        
                    #OutFile.write(final_answer)
#answer_list.append(final_answer)


days_in_month_list = []

list_count = 0

SumVar2 = 0
Count2 = 0
Sum_Average_list = []
#for i in answer_list:
#    count2 += 1
#    print i + ' ' + str(count2)
#for i in range(len(answer_list)):
"""for y in range(2006, 2010):
    
    for x in range(1,13):
        
        for i in range(len(answer_list)):
            year2_type = int(answer_list[i][:4])
            month2_type = int(answer_list[i][5:7])
            data2_type = len(answer_list[i])
            SumVar2 = 0
            if y == year2_type and x == month2_type:
                #print data2_type
                #SumVar2 += data2_type
                Count2 += 1
                print data2_type, answer_list[i], Count2, y
                #Count2 += 1,
                #answers_f = SumVar2/Count2
                #print y, x, SumVar2, Count2, answers_f
                
            #print SumVar2
        days_in_month_list.append(Count2)
        Count2 = 0
                #For_Real_Final_Answer_this_time = SumVar2/Count2
                #print Count2
            #Summation_average_list.append(For_Real_Final_Answer_this_time)"""
        
                        
#month_count = 0
#for y2 in range(2006, 2010):
#    for months2 in range(1,13):
#        month_count += 1
#        print str(y2) + ' ' + str(months2) + ' ' + str(Summation_average_list[month_count-1])"""

#        month_count += 1
        #print str(y) + ' ' + str(months) + ' ' + str(answer_list[month_count-3])
        #print answer_list[month_count-1]
#for iterator in days_in_month_list:
#    print iterator
#for i in answer_list:
#    print i
ReadFile.close()
OutFile.close()
