import pyGDP 
 
 
pyGDP = pyGDP.pyGDPwebProcessing() 
 
 
""" 
6 This example shows how to use multiple dataTypes and Statistics. 
7  
"""  

submitFeatureWeightGridStatistics(self, geoType, dataSetURI, varID, startTime, endTime,

    attribute='the_geom', value=None, gmlIDs=None,

    verbose=None, coverage='true', delim='COMMA', stat='MEAN',                     

    grpby='STATISTIC',timeStep='false', summAttr='false')

  

"""

Makes a featureWeightedGridStatistics algorithm call. 

"""

         

inputs = [("FEATURE_ATTRIBUTE_NAME",attribute), 

            ("DATASET_URI", dataSetURI), 

            ("DATASET_ID", varID), 

            ("TIME_START",startTime),

            ("TIME_END",endTime), 

            ("REQUIRE_FULL_COVERAGE",coverage), 

            ("DELIMITER",delim), 

            ("STATISTICS",stat), 

            ("GROUP_BY", grpby),

            ("SUMMARIZE_TIMESTEP", timeStep), 

            ("SUMMARIZE_FEATURE_ATTRIBUTE",summAttr), 

            ("FEATURE_COLLECTION", featureCollection)] 

