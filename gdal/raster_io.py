"""Some examples of reading a raster file in, manipulating it and 
   writing it back out. Also contains some info on how to alter the 
   geotransform (extent) and to set a new projection system
   @Chris Williams 22/09/15"""


from osgeo import gdal, gdalconst, osr
from osgeo.gdalconst import * 
import matplotlib.pyplot as pyplot

########################################
# WRITE DATA IN

#create driver (determines the file format)
driver = gdal.GetDriverByName('Gtiff')
driver.Register()

#read in fdata
file_name='O:/Desktop/python_meeting_group/aoi2_432_merge.tif'
inDs = gdal.Open(file_name, GA_ReadOnly)

#get dimension info
cols = inDs.RasterXSize
rows = inDs.RasterYSize
bands = inDs.RasterCount

#get geotransform
geotransform = inDs.GetGeoTransform()

#get projection info
proj = inDs.GetProjection()

#Count how many bands there are available
inDs.RasterCount

#Get band(s)
band = inDs.GetRasterBand(1)

#Read in band as an array
image_array = band.ReadAsArray(0, 0, cols, rows)

#Display array using matplotlib
'''
plt.imshow(image_array)
plt.colorbar()
plt.show()
'''

########################################
# Some array manipulation 
image_array=image_array*100

########################################
# WRITE DATA OUT

# Creates a new raster data source
file_out='O:/Desktop/python_meeting_group/test_out_4.tif'
rows, cols = image_array.shape
bands = 1

outDs = driver.Create(file_out, cols, rows, bands, gdal.GDT_Float32)

#Set geotransform info
outDs.SetGeoTransform(geotransform) # using the same geotransform info as was passed in

#Set projection info
outDs.SetProjection(inDs.GetProjection()) # using the same projection info as was passed in

#Write out the band data
outBand = outDs.GetRasterBand(1)
outBand.WriteArray(image_array)

#Flush everything out
outDs=None

############## 
## One way of defining a new geotransform
'''
geotransform = np.zeros(6)
geotransform[0] = tl_x
geotransform[1] = post
geotransform[2] = rotation
geotransform[3] = tl_y
geotransform[4] = rotation
geotransform[5] = -post
geotransform=geotransform.tolist()
'''
#############################
## Setting new projection info
## Many ways to do this
## Look here also:
## http://www.gdal.org/osr_tutorial.html
## http://www.epsg-registry.org/
## http://geoexamples.blogspot.co.uk/2012/01/creating-files-in-ogr-and-gdal-with.html
'''
spatialReference = osr.SpatialReference()
spatialReference.ImportFromProj4("+proj=stere +lat_0=90 +lat_ts=71 +lon_0=-39 +k=1 +x_0=0 +y_0=0 +datum=WGS84 +units=m +no_defs") 
#spatialReference.SetWellKnownGeogCS( "EPSG:4326" )
#spatialReference.ImportFromEPSG(4326)
prj=spatialReference.ExportToWkt()
outDs.SetProjection(prj)
'''