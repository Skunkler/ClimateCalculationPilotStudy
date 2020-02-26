import os, csv, sys

workspace = r"H:\Keely_PythonProject\NetCDF\McCarran_point\CMCC-CMS\historical\AnnualAverage"

#outFile = open(r"H:\Keely_PythonProject\compiled_Tables\test2.csv", 'a')


count = 0
            
for root, dirs, files in os.walk(workspace):
    for filename in files:
        if 'pr' in filename or 'asmax' in filename or 'asmin' in filename:

            
            OutFile = open(root + '\\' + filename[:-4] + '.txt', 'w')

            readfile = root + '\\' + filename

            Lower_Lim_Label = "Lower_Limit_95%_confidence"
            Mean_label = "Annual_Mean"
            Upper_Lim_Label = "Upper_Limit_95%_confidence"
            
            
                
            csv_file = csv.reader(open(readfile, "rb"), delimiter=",")
            for row in csv_file:
                
                try: 
                    Annual_mean = row[1]
                    Lower_lim = row[5]
                    Upper_lim = row[6]
                    OutFile.write(str(round(float(Lower_lim),2)) + ',' + str(round(float(Annual_mean),2)) + ',' + str(round(float(Upper_lim),2)) + '\n')
                    
                    
                except:
                    
                    OutFile.write(filename[:-4] + ',' + filename[:-4] + ',' + filename[:-4] + '\n' + 'lower lim,annual_mean,upper_lim' + '\n')
                    

            count += 1
            OutFile.close()

                

#OutFile = open(r"H:\Keely_PythonProject\compiled_Tables\test3.csv", 'w')

    


