import os, csv, sys

workspace = r"H:\Keely_PythonProject\NetCDF\McCarran_point\CNRM-CM5\historical\GCMF_GCMC_1971_2000\ChangeFactor2"

#outFile = open(r"H:\Keely_PythonProject\compiled_Tables\test2.csv", 'a')



count = 0
            
for root, dirs, files in os.walk(workspace):
    for filename in files:
        if 'Change_factor' in filename:

            
            OutFile = open(root + '\\' + filename[:-4] + '.txt', 'w')

            readfile = root + '\\' + filename

            
            
            
                
            csv_file = csv.reader(open(readfile, "rb"), delimiter=",")
            for row in csv_file:
                
                try: 
                    Change_factor = row[1]
                    #print Change_factor
                    OutFile.write(str(round(float(Change_factor),2)) + '\n')
                    
                    
                except:
                    
                    OutFile.write(filename[14:-4] + '\n')
                    

            count += 1
            OutFile.close()

    


