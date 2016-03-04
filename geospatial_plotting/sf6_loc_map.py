import numpy as np
from scipy import ndimage
from scipy import interpolate
from scipy.stats import nanmedian
from matplotlib import rcParams
import matplotlib.pyplot as plt
import matplotlib
import os
from shapely.geometry import Point, Polygon, MultiPoint, MultiPolygon, LineString
from matplotlib.collections import PatchCollection
import pandas as pd
from descartes import PolygonPatch
import matplotlib.image as mpimg
import matplotlib.patches as patches
import matplotlib.gridspec as gridspec

import plotmap
import georaster
import shapefile

rcParams['font.sans-serif'] = 'Arial'
rcParams['font.size'] = 6
rcParams['mathtext.fontset'] = 'stixsans'


fig = plt.figure(figsize=(5,5.5))

gs = gridspec.GridSpec(2, 2,
                       width_ratios=[1.5,1],
                       height_ratios=[1,1]
                       )


########## LOCATION MAP ##############

region = (-50.5,-47.6,66.6,67.4)

## Plot the map
ax = plt.subplot(gs[:-1,:])
lon_0 = region[0] + (region[1]-region[0])
mapo = plotmap.Map(extent=region,lon_0=lon_0,fig=fig,ax=ax)

# Define ocean colour
mapo.ax.patch.set_facecolor('#C8EBFF')

# Ocean/Coast
shp_info = mapo.map.readshapefile('D:\dems\Gimp_Ocean_Mask_240m_EPSG4319',
						 'ocean',drawbounds=False)

df_ocean = pd.DataFrame({
	'poly': [Polygon(xy) for xy in mapo.map.ocean],
	'DN': [f['DN'] for f in mapo.map.ocean_info]
	})
df_ocean = df_ocean[df_ocean['DN'] == 0]
# draw ward patches from polygons
df_ocean['patches'] = df_ocean['poly'].map(lambda x: PolygonPatch(
	    x,
	    fc='#ACD0A5', # Land colour #FFEDA0
	    ec='none', lw=.25, alpha=.9))

# plot coast by adding the PatchCollection to the axes instance
mapo.ax.add_collection(PatchCollection(df_ocean['patches'].values, match_original=True))

# Ice area
shp_info = mapo.map.readshapefile('D:\dems\Gimp_Ice_Mask_240m_EPSG4319',
						 'ice',drawbounds=False)

df_ice = pd.DataFrame({
	'poly': [Polygon(xy) for xy in mapo.map.ice],
	'DN': [f['DN'] for f in mapo.map.ice_info]
	})
df_ice = df_ice[df_ice['DN'] == 1]
# draw ward patches from polygons
df_ice['patches'] = df_ice['poly'].map(lambda x: PolygonPatch(
	    x,
	    fc='#F9F9F9',
	    ec='none', lw=.25, alpha=1,zorder=99))

# plot coast by adding the PatchCollection to the axes instance
mapo.ax.add_collection(PatchCollection(df_ice['patches'].values, match_original=True))	


# Elevation contours GIMP_DEM_WRS008012_EPSG4319
shp_info = mapo.map.readshapefile('D:\dems\Gimp_DEM_Ice_500m_contours_simple',
 							 'contours',drawbounds=False)
for shape,shapedict in zip(mapo.map.contours,mapo.map.contours_info):
	if shapedict['elev'] <= 400:
		continue
	xx,yy = zip(*shape)
	mapo.map.plot(xx,yy,'black',linewidth=0.5,alpha=0.9,zorder=102)

# Label the contours ... need to come up with a nice way of doing this!!
plt.annotate(600,xy=mapo.map(-49.88,67.3),rotation=-100,alpha=0.9,zorder=103)
plt.annotate(800,xy=mapo.map(-49.75,67.29),rotation=-100,alpha=0.9,zorder=103)
plt.annotate(1000,xy=mapo.map(-49.52,67.28),rotation=-90,alpha=0.9,zorder=103)
plt.annotate(1200,xy=mapo.map(-49.15,67.28),rotation=-90,alpha=0.9,zorder=103)
plt.annotate(1400,xy=mapo.map(-48.63,67.28),rotation=-90,alpha=0.9,zorder=103)
plt.annotate(1600,xy=mapo.map(-47.88,67.265),rotation=-70,alpha=0.9,zorder=103)


# Hydrological catchment
patches = []
shp_info = mapo.map.readshapefile('D:\dems\\rastert_basin_f4_WGS84',
 							 'basin',drawbounds=False)
df_catch = pd.DataFrame({
	'poly': [Polygon(xy) for xy in mapo.map.basin]
	#'DN': [f['DN'] for f in mapo.map.basin_info]
	})
#df_basin = df_basin[df_basin['DN'] == 1]
# draw ward patches from polygons
df_catch['patches'] = df_catch['poly'].map(lambda x: PolygonPatch(
	    x,
	    fc='#D6D6D6',
	    ec='none', lw=.25, alpha=.9,zorder=99))

mapo.ax.add_collection(PatchCollection(df_catch['patches'].values, match_original=True))	


# Glacier labels
plt.annotate('RG',xy=mapo.map(-50.36,67.08),rotation=0,zorder=105)
plt.annotate('LG',xy=mapo.map(-50.34,67.04),rotation=0,zorder=105)
# Proglacial sample point
x,y = mapo.map(-50.2,67.07)
plt.plot(x,y,'^k',markersize=3)
# Moulin point
x,y = mapo.map(-49.274,66.964)
plt.plot(x,y,'s',mfc='#E41A1C',markersize=4,mec='none')


# Lat/Lon Grid. Order of spacing: x, y
mapo.geo_ticks(1,0.4,rotate_parallels=True)


# Scale bar.
lonll, lonur, latll, latur = mapo.extent
xloc = lonll + 0.89*(lonur-lonll)
yloc = latll + 0.12*(latur-latll)
scale = mapo.map.drawmapscale(xloc,yloc,(lonur+lonll)/2,(latur+latll)/2,20,
                 barstyle='fancy',fontsize=rcParams['font.size'],
                 fillcolor1='black',fillcolor2='white',fontcolor='black',yoffset=1700) ##525252
for item in scale:
	try:
		item.set_linewidth(0.5)
	except:
		continue


# Remove border from axis
for axis in ['top','bottom','left','right']:
	mapo.ax.spines[axis].set_linewidth(0)


# Greenland context figure
# left, bottom, width, height
ax_inset = fig.add_axes([0.15,0.53,0.22,0.16])
ax_inset.set_axis_bgcolor('none')
for axis in ['top','bottom','left','right']:
	ax_inset.spines[axis].set_linewidth(0)
im = mpimg.imread('gris_context.png')
ax_inset.imshow(im,interpolation='none')
ax_inset.set_xticks([])
ax_inset.set_yticks([])

# Label
ax.annotate('a', xy=(0.03,0.95), xycoords='axes fraction', fontweight='bold',
               horizontalalignment='left', verticalalignment='top',
               bbox=dict(lw=0.5,boxstyle="square",ec='k',fc='white'))



######### MOULIN MAP #############

ax3 = plt.subplot(gs[2])

region = (-49.29,-49.25,66.958,66.98)
lon_0 = -45

## Plot the map
lon_0 = region[0] + (region[1]-region[0])
mapo2 = plotmap.Map(extent=region,lon_0=lon_0,fig=fig,ax=ax3)

# Lat/Lon Grid. Order of spacing: x, y
mapo2.geo_ticks(0.02,0.01,rotate_parallels=True)


# Moulin point
x,y = mapo2.map(-49.270183,66.969500)
plt.plot(x,y,'o',mfc='gray',markersize=4,mec='none')
plt.annotate('M11',xy=(x+80,y-40),color='gray')

x,y = mapo2.map(-49.274,66.964)
plt.plot(x,y,'o',mfc='#377EB8',markersize=4,mec='none')
plt.annotate('M12',xy=(x-240,y-40),color='#377EB8')

# GPS points
locs = pd.read_csv('gps_loc_dec_plot.csv')
for i,site in locs.iterrows():
	x,y = mapo2.map(site['lon'],site['lat'])
	plt.plot(x,y,'+',markersize=5,mec='#E41A1C',mfc='#E41A1C')
	if site['id'] == 4:
		xchange = -80
		ychange = -80
	elif site['id'] == 1:
		xchange = -100
		ychange = -70
	elif site['id'] == 3:
		xchange = 20
		ychange = -100
	else:
		xchange = 20
		ychange = 20
	plt.annotate("%d" %(site['id']),xy=(x+xchange,y+ychange),rotation=0,alpha=1,zorder=105,color="#E41A1C")


# Scale bar.
lonll, lonur, latll, latur = mapo2.extent
xloc = lonll + 0.5*(lonur-lonll)
yloc = latll + 0.07*(latur-latll)
scale = mapo2.map.drawmapscale(xloc,yloc,(lonur+lonll)/2,(latur+latll)/2,1,
                 barstyle='simple',fontsize=rcParams['font.size'],
                 fontcolor='black',zorder=106) ##525252
for item in scale:
	try:
		item.set_linewidth(0.5)
	except:
		continue


ax3.annotate('b', xy=(0.05,0.95), xycoords='axes fraction', fontweight='bold',
               horizontalalignment='left', verticalalignment='top')

# Thin the border
for axis in ['top','bottom','left','right']:
	ax3.spines[axis].set_linewidth(0.5)

# Tuck the little map up underneath main map
pos = ax3.get_position()
new_pos = [pos.x0+0.02, pos.y0+0.035, pos.width, pos.height]
ax3.set_position(new_pos)



######### MOULIN PHOTO ###############
ax2 = plt.subplot(gs[3])
im = mpimg.imread('moulin_pic.jpg')
ax2.imshow(im,interpolation='none')
ax2.set_xticks([])
ax2.set_yticks([])
ax2.annotate('c', xy=(0.05,0.95), xycoords='axes fraction', fontweight='bold',
               horizontalalignment='left', verticalalignment='top',color="white")

# Thin the border
for axis in ['top','bottom','left','right']:
	ax2.spines[axis].set_linewidth(0.5)

# Tuck the photo in to line up with RHS of map
pos = ax2.get_position()
new_pos = [pos.x0-0.095, pos.y0+0.095, pos.width, pos.height]
ax2.set_position(new_pos)


## Save etc

#pl.subplots_adjust(left=0.1,right=0.8,top=0.95,bottom=0.05)
plt.savefig('sf6_loc_map.pdf',dpi=300)
plt.savefig('sf6_loc_map.png',dpi=300)
plt.close()