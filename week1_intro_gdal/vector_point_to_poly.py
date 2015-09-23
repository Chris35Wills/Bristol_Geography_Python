"""Read in points and create polygon in a shapefile format
   Makes use of the pandas, matplotlib, osgeo.ogr and 
   osgeo.osr packages
   @Chris Williams 22/09/15"""

import matplotlib.pyplot as plt
import pandas as pd

from osgeo import ogr
from osgeo import osr

##############################################
# Read in data using pandas
drainage_xy=pd.read_csv('O:/Desktop/python_meeting_group/point_outline.txt', delim_whitespace=True, skiprows=7, names=['fid','x','y'])
fid=drainage_xy['fid'].values
x=drainage_xy['x'].values
y=drainage_xy['y'].values

# View data
plt.scatter(x,y)
plt.show()

# Creat driver and dataset
DriverName='ESRI Shapefile'
driver=ogr.GetDriverByName(DriverName) ## http://www.gdal.org/ogr_formats.html - make sure to use type where creation option is set to YES
shapeData=driver.CreateDataSource('O:/Desktop/python_meeting_group/test_poly_5.shp')

#Set projection
spatialReference = osr.SpatialReference()
spatialReference.ImportFromProj4("+proj=stere +lat_0=90 +lat_ts=71 +lon_0=-39 +k=1 +x_0=0 +y_0=0 +datum=WGS84 +units=m") #jons proj

#Create layer
layer = shapeData.CreateLayer('layer1', spatialReference, ogr.wkbPolygon)
layerDefinition = layer.GetLayerDefn()

#Create ring from points
boundary = ogr.Geometry(ogr.wkbLinearRing)

##add points to ring
for i in range(len(fid)):
	boundary.AddPoint(x[i],y[i])
boundary.CloseRings()

#add ring to polygon geometry object 
poly=ogr.Geometry(ogr.wkbPolygon)
poly.AddGeometry(boundary)
poly.GetGeometryCount()

# Put layer inside feature
featureIndex = 0
feature = ogr.Feature(layerDefinition)
feature.SetGeometry(poly)
feature.SetFID(featureIndex)

#Put feature in a layer
layer.CreateFeature(feature)

#Flush everything out
shapeData.Destroy()
##############################################

"""
Useful websites regarding coordinate transforms in python:

http://www.gis.usu.edu/~chrisg/python/2008/os2_slides.pdf
http://pyproj.googlecode.com/svn/trunk/docs/index.html
http://all-geo.org/volcan01010/2012/11/change-coordinates-with-pyproj/

http://invisibleroads.com/tutorials/gdal-shapefile-points-save.html << this is the most useful link
http://geoexamples.blogspot.co.uk/2012/01/creating-files-in-ogr-and-gdal-with.html
"""