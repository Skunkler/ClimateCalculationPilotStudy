import arcpy, os
from arcpy import env
arcpy.env.overwriteOutput=True


NetCDF_location = r'H:\Keely_PythonProject\NetCDF\McCarran_point\CNRM-CM5\future\rcp45'

if not os.path.exists(NetCDF_location + '\\csv'):
        os.mkdir(NetCDF_location + '\\csv')

env.workspace = NetCDF_location


for root, dirs, files in os.walk(NetCDF_location):
    for name in files:
        if name[-3:] == '.nc':
            if 'pr' in name:
                Variables = "pr;time"
                outTableView = "PR_View"
                rowDimension = "time"
                dimensionValue = ""
                valueSelectionMethod = "BY_VALUE"
                arcpy.MakeNetCDFTableView_md(root + '\\' + name, Variables, outTableView, rowDimension, dimensionValue, valueSelectionMethod)
            elif 'tasmax' in name:
                Variables = "tasmax;time"
                outTableView = "Tasmax_View"
                rowDimension = "time"
                dimensionValue = ""
                valueSelectionMethod = "BY_VALUE"
                arcpy.MakeNetCDFTableView_md(root + '\\' + name, Variables, outTableView, rowDimension, dimensionValue, valueSelectionMethod)
            elif 'tasmin' in name:
                Variables = "tasmin;time"
                outTableView = "Tasmin_View"
                rowDimension = "time"
                dimensionValue = ""
                valueSelectionMethod = "BY_VALUE"
                arcpy.MakeNetCDFTableView_md(root + '\\' + name, Variables, outTableView, rowDimension, dimensionValue, valueSelectionMethod)

   
