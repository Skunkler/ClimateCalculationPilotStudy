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

dataSetURI = 'http://cida.usgs.gov/thredds/dodsC/loca_future'

datatypes = pyGDP.getDataType(dataSetURI)

outputpath_earlys=list()
DataTypes_list = ['tasmax_ACCESS1-0', 'tasmin_ACCESS1-0','tasmax_CanESM2','tasmin_CanESM2', 'tasmax_CCSM4', 'tasmin_CCSM4', 'tasmax_CESM1-BGC', 'tasmin_CESM1-BGC', 'tasmax_CMCC-CMS',\
                  'tasmin_CMCC-CMS', 'tasmax_CNRM-CM5', 'tasmin_CNRM-CM5', 'tasmax_GFDL-CM3', 'tasmin_GFDL-CM3', 'tasmax_HadGEM2-CC', \
                  'tasmin_HadGEM2-CC', 'tasmax_HadGEM2-ES', 'tasmin_HadGEM2-ES', 'tasmax_MIROC-ESM-CHEM', 'tasmin_MIROC-ESM-CHEM', 'tasmax_MIROC-ESM', \
                  'tasmin_MIROC-ESM', 'tasmax_CSIRO-Mk3-6-0', 'tasmin_CSIRO-Mk3-6-0', 'tasmax_GFDL-ESM2M', 'tasmin_GFDL-ESM2M']


for Type_item in DataTypes_list:
    for datatype in datatypes:
        if Type_item in datatype and 'rcp45' in datatype:
            outName = 'Loca_rcp45_' + datatype + '.csv'
            if os.path.isfile(outName):
                outputpath_earlys.append(outputPath)
            else:
                outputPath = pyGDP.submitFeatureWeightedGridStatistics(shapefile, dataSetURI, datatype, '2006-01-01', '2100-12-31', polyAttribute, polyValue, outputfname = outName)
                print(outputPath)
        elif Type_item in datatype and 'rcp85' in datatype:
            outName = 'Loca_rcp85_' + datatype + '.csv'
            if os.path.isfile(outName):
                outputpath_earlys.append(outputPath)
            else:
                outputPath = pyGDP.submitFeatureWeightedGridStatistics(shapefile, dataSetURI, datatype, '2006-01-01', '2100-12-31', polyAttribute, polyValue, outputfname = outName)
                print(outputPath)
        
       
