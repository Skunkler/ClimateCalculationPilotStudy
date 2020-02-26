import matplotlib.dates as mdates

import numpy

import pylab

from pylab import plot, show

import pyGDP

import array

pyGDP = pyGDP.pyGDPwebProcessing()


userPoly = [(-102.8184, 39.5273), (-102.8184, 37.418), (-101.2363, 37.418), (-101.2363,39.5273), (-102.8184, 39.5273)]

baseURI = "http://cida.usgs.gov/thredds/dodsC/loca_future"
#'dods://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/NARR.dailyavgs/monolevel/air.2m.'

varID = 'air'


kelvinConst = 273.15     # degree conversion from kelvin to centigrade

year_0 = 1979

year_1 = 1990

years = array.array('i',(i for i in range(year_0,year_1+1)))

fileList = []


for yr in years:

    datasetURI = '%s%s%s' % (baseURI,yr,'.nc')

    timeRange = pyGDP.getTimeRange(datasetURI,varID)

    timeStart = timeRange[0]

    timeEnd   = timeRange[1]

    print('begining process request for %s on year %s' % (varID, yr))

    outputFile_handle = pyGDP.submitFeatureWeightedGridStatistics(userPoly, datasetURI, varID, timeStart, timeEnd)

    fileList.append(outputFile_handle)


fig = pylab.figure(figsize=(12,6),facecolor='w')

ax = fig.gca()

ax.set_ylabel('Air Temperature (C)')

ax.plot_date(dates,vals,'b-')

ax.xaxis.set_major_locator(mdates.YearLocator(5,month=1,day =1))

ax.xaxis.set_major_formatter(mdates.DateFormatter(' %Y'))

show()    
