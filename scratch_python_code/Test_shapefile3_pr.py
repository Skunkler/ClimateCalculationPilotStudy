import pyGDP
import numpy
import pylab
import array
import glob
import os
import matplotlib.dates as mdates


pyGDP = pyGDP.pyGDPwebProcessing()

shapefile = 'upload:Final_Compiled_LOCA_Points_of_interest_buffer200'



attributes = pyGDP.getAttributes(shapefile)

for attr in attributes:
    print attr

polyAttribute = 'Name'

values = pyGDP.getValues(shapefile, polyAttribute)

for v in values:
    print v

polyValue = 'BD_Mtn'

dataSetURI = 'http://cida.usgs.gov/thredds/dodsC/loca_historical'

datatypes = pyGDP.getDataType(dataSetURI)

outputpath_earlys=list()
DataTypes_list = ['pr_ACCESS1-0','pr_CanESM2', 'pr_CCSM4', 'pr_CESM1-BGC', 'pr_CMCC-CMS',\
                  'pr_CNRM-CM5', 'pr_GFDL-CM3', 'pr_HadGEM2-CC', \
                  'pr_HadGEM2-ES', 'pr_MIROC-ESM-CHEM', 'pr_MIROC-ESM', \
                  'pr_CSIRO-Mk3-6-0', 'pr_GFDL-ESM2M']


for Type_item in DataTypes_list:
    for datatype in datatypes:
        if Type_item in datatype:
            outName = 'Loca_Historical_' + datatype + '.csv'
            if os.path.isfile(outName):
                outputpath_earlys.append(outputPath)
            else:
                outputPath = pyGDP.submitFeatureWeightedGridStatistics(shapefile, dataSetURI, datatype, '1950-01-01', '2005-12-31', polyAttribute, polyValue, outputfname = outName)
                print(outputPath)
        
       
