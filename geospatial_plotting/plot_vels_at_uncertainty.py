import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
import pandas as pd
from matplotlib.collections import PatchCollection
from shapely.geometry import Point, Polygon, MultiPoint, MultiPolygon, LineString
from descartes import PolygonPatch

import georaster
import plotmap

rcParams['font.sans-serif'] = 'Arial'
rcParams['font.size'] = 6
rcParams['mathtext.fontset'] = 'stixsans'

err_thresh = 60.
mask = georaster.SingleBandRaster('/home/s1144267/rds/landsat/WRS12_annual/merge_1985_1986_snr4_rad340_nmin1_region_v3_pstere.mask.TIF')
dem = georaster.SingleBandRaster('/home/s1144267/rds/landsat/WRS12_annual/GIMP_dem_WRS12_merge_240m_pstere.TIF')

mask_vel = np.where((dem.r >= 400) & (dem.r <= 1100) & (mask.r == 1),1,0)
ntot = np.sum(mask_vel)

region = (-51.1,-49.2,67.450714,69.2)
lon_0 = -45

# Ice area
ice_mapo = plotmap.Map(extent=region,lon_0=lon_0)
shp_info = ice_mapo.map.readshapefile('Gimp_Ice_Mask_240m_EPSG4319',
						 'ice',drawbounds=False)

df_ice = pd.DataFrame({
	'poly': [Polygon(xy) for xy in ice_mapo.map.ice],
	'DN': [f['DN'] for f in ice_mapo.map.ice_info]
	})
df_ice = df_ice[df_ice['DN'] == 1]
# draw ward patches from polygons
df_ice['patches'] = df_ice['poly'].map(lambda x: PolygonPatch(
	    x,
	    fc='#BDBDBD',
	    ec='none', lw=.25, alpha=.9,zorder=99))
ice_mapo = None
plt.close()

fig = plt.figure(figsize=(8,6))

with open('list_merge_files_v4.txt','r') as fh:

	n = 1
	for merge_file in fh:

		merge_file = merge_file.strip()

		if int(merge_file[6:10]) == 1985 and int(merge_file[11:15]) == 1994:
			continue
		if int(merge_file[6:10]) == 2007 and int(merge_file[11:15]) == 2014:
			continue

		im = georaster.SingleBandRaster(merge_file)
		im_err = georaster.SingleBandRaster(merge_file.replace('.vel','.err'))

		mask_temp = np.where((mask_vel == 1) & (im_err.r < err_thresh),1,0)
		frac = float(np.sum(mask_temp)) / ntot

		if frac < 0.35:
			continue

		retained_vel = np.where(mask_temp == 1, im.r, np.nan)
		
		ax = plt.subplot(3,6,n)

		mapo = plotmap.Map(extent=region,lon_0=lon_0,fig=fig,ax=ax)
		#mapo = plotmap.Map(extent=region,lon_0=lon_0,figsize=(2,2.5))

		# plot ice by adding the PatchCollection to the axes instance
		mapo.ax.add_collection(PatchCollection(df_ice['patches'].values, match_original=True))	

		plt.imshow(retained_vel,
				   cmap='YlGnBu_r',vmin=0,vmax=300,
				   interpolation='none',
				   extent=im.get_extent_projected(mapo.map),zorder=100)

		year_start = merge_file[6:10]
		year_end = merge_file[11:15]
		label = year_start + '-' + year_end
		mapo.ax.annotate(label,fontsize=8, fontweight='bold', xy=(-0.1,1.15), xycoords='axes fraction',
           horizontalalignment='left', verticalalignment='top',zorder=101)

		if n in [1,]:
			mapo.geo_ticks(2,0.7,rotate_parallels=True)
		else:
			mapo.geo_ticks(2,0.7,rotate_parallels=True,
				mlabels=[0,0,0,0],plabels=[0,0,0,0])
		#Remove border from axis
		for axis in ['top','bottom','left','right']:
			mapo.ax.spines[axis].set_linewidth(0)

		n += 1
		# plt.savefig(merge_file.replace('.vel.TIF','.vel_60myr.png'),dpi=300)
		# plt.close()

plt.subplots_adjust(hspace=0.26)
plt.savefig('all_periods_60myr.png',dpi=300)
plt.close()

