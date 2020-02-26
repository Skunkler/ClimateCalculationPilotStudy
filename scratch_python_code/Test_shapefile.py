import pyGDP
import numpy
import pylab
import array
import glob
import os
import matplotlib.dates as mdates


pyGDP = pyGDP.pyGDPwebProcessing()

shapefile = 'upload:Compiled_LOCA_Climate_Points_of_interest_buffer200'



attributes = pyGDP.getAttributes(shapefile)

for attr in attributes:
    print attr

polyAttribute = 'name'

values = pyGDP.getValues(shapefile, polyAttribute)

for v in values:
    print v

polyValue = 'EAST CENTRAL MOUNTAINS'

dataSetURI = 'http://cida.usgs.gov/thredds/dodsC/loca_future'

datatypes = pyGDP.getDataType(dataSetURI)

outputpath_earlys=list()
outputpath_lates=list()

for datatype in datatypes:
    if 'rcp85' in datatype:
    #if 'tasmax' in datatype and 'rcp85' in datatype:
        print(datatype)
        outName = 'Loca_early_Future_' + datatype + '.csv'
        if os.path.isfile(outName):
            outputpath_earlys.append(outputPath)
        else:
            outputPath = pyGDP.submitFeatureWeightedGridStatistics(shapefile, dataSetURI, datatype, '2006-01-01T00:00:00Z', '2009-12-31T00:00:00Z', polyAttribute, polyValue, outputfname = outName)
            print(outputPath)
            outputpath_earlys.append(outputPath)
            outName = 'Loca_late_Feature_' + datatype + '.csv'
        if os.path.isfile(outName):
            outputpath_lates.append(outputPath)
        else:
            outputPath = pyGDP.submitFeatureWeightedGridStatistics(shapefile, dataSetURI, datatype, '2096-01-01T00:00:00Z', '2099-12-31T00:00:00Z', polyAttribute, polyValue, outputfname = outName)
            print(outputPath)
            outputpath_lates.append(outputPath)
#outputPath = pyGDP.submitFeatureWeightedGridStatistics(shapefile, dataSetURI, datatypes, '2006-01-01T12:00:00Z', '2007-01-01T00:00:00Z', polyAttribute, polyValue) 



"""for dt in datatypes:
    print dt
timeRange = pyGDP.getTimeRange(dataSetURI, datatypes[1])
for t in timeRange:
    print t"""
