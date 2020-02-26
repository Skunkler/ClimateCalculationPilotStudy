import os

ReadFile = open(r"H:\Keely_PythonTest_Output\Loca_early_Future_tasmax_CanESM2_r1i1p1_rcp85.csv", 'r')
OutFile = open(r"H:\Keely_PythonTest_Output\Loca_Test_log.txt", 'w')


my_list = []

for i in ReadFile:
    my_list.append(i)

count = 0
count2 = 0
sumVar1 = 0

#"""for i in range(3, len(my_list)):
 #   month = my_list[i][5:7]
  #  year = my_list[i][0:4]
  #  year_type = int(year)
  #  month_type = int(month)
  #  data = my_list[i][21:30]
  #  data_type = float(data)
  #  if year_type == 2006 and month_type == 1:
  #      count += 1
  #      sumVar1 += data_type
  #  print "2006 January average max temp in degrees celsius is: " + str(sumVar1/count)
  #  year_type += 1
  #  month_type += 1"""

year_type = 2006
for i in range(3, len(my_list)):
    month = my_list[i][5:7]
    month_type = int(month)
    data = my_list[i][21:30]
    data_type = float(data)
    year = int(my_list[i][0:4] 
    if month_type == 1
        count += 1
        sumVar1 += float(my_list[i][21:30])
        i += 1
    count = 0
    sumVar1 = 0
    print "The monthly time step for " + str(my_list[i][0:4]) + " is " + str(sumVar1/count)



#    """avg = sumVar1/count
#        OutFile.write(str(year_type) + " and the month is " + str(month_type) + " average is " + str(avg) + '\n')
#        year_type += 1
#        count = 0
#        sumVar1 = 0
#OutFile.close()"""

        
