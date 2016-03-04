# Loading and plotting raster data

Andrew Tedstone, 3 March 2016

I introduced a couple of modules/classes that I have written to simplify visualising, examining and plotting raster data.

georaster - https://github.com/atedstone/georaster - this class makes it easy to load any raster supported by GDAL into Python, either interactively or as part of a script. Quick example (for more info see readme and all the comments in the code):

	import georaster
	my_image = georaster.SingleBandRaster('myfile.tif')
	print my_image.extent
	print my_image.get_extent_latlon()


plotmap - https://github.com/atedstone/plotmap - this class simplifies the plotting of maps, particularly with raster data, using the Matplotlib basemap module as its base. See the basic readme provided in the repository for more info.

In addition I've put up a couple of scripts and associated maps that are reasonably well commented in order to show how you can use these classes for real, likely to be particularly useful in the case of plotmap.