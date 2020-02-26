import pyGDP


pyGDP = pyGDP.pyGDPwebProcessing()

geoType = [(-119.871972, 34.420668), (-119.843353, 34.421090), (-119.844263, 34.406818), (-119.878692, 34.408690)]


baseURI = 'http://cida.usgs.gov/thredds/dodsC/loca_future'
startTime = 1950
endTime = 2100
varID = 'pr_CCSM4_r6i1p1_rcp45'

#['tasmax_CCSM4_r6i1p1_rcp45', 'tasmin_CCSM4_r6i1p1_rcp45']

years = array.array('i', (i for i in range(startTime, endTime+1)))
fileList = []

for yr in years:
    datasetURI = '%s%s%s' % (baseURI, yr, '.nc')
    timeRange = pyGDP.getTimeRange(datasetURI, varID)
    timeStart = timeRange[0]
    timeEnd = timeRange[1]
    print "process beginning for %s on year %s'" % (varID, yr)
    outputFile_handle = pyGDP.submitFeatureWeightedGridStatistics(self, geoType, dataSetURI, varID, startTime, endTime, '', '', '', '', coverage='true', delim = 'COMMA')
    fileList.append(outputFile_handle)
