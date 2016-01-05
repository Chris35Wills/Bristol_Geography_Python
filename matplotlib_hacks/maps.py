#!/usr/bin/python 
from mpl_toolkits.basemap import Basemap
import numpy as np
import brewer2mpl

def globalMap():
    # draws the global map
    # map = Basemap(projection='ortho',lat_0=5,lon_0=-30,resolution='l')
    map = Basemap(projection='mill',llcrnrlat=-80,urcrnrlat=80,llcrnrlon=-30,urcrnrlon=330,resolution='c') # a global projection centred on Greenwich
    # draw coastlines, country boundaries, fill continents.
    map.drawcoastlines(linewidth=0.25)
    map.fillcontinents(color=[.91,.91,.95],zorder=0)
    # draw the edge of the map projection region (the projection limb)
    # map.drawmapboundary(fill_color='aqua')
    # draw lat/lon grid lines every 30 degrees.
    map.drawmeridians(np.arange(0,360,30))
    map.drawparallels(np.arange(-90,90,30))
    return map

def myMap(lonW,lonE,latS,latN):
    # draws the global map
    # map = Basemap(projection='ortho',lat_0=5,lon_0=-30,resolution='l')
    map = Basemap(projection='mill',llcrnrlat=latS,urcrnrlat=latN,llcrnrlon=lonW,urcrnrlon=lonE,resolution='c') # a global projection centred on Greenwich
    # draw coastlines, country boundaries, fill continents.
    map.drawcoastlines(linewidth=0.25)
    map.fillcontinents(color=[.91,.91,.95],zorder=0)
    # draw the edge of the map projection region (the projection limb)
    # map.drawmapboundary(fill_color='aqua')
    # draw lat/lon grid lines every 30 degrees.
    map.drawmeridians(np.arange(0,360,30))
    map.drawparallels(np.arange(-90,90,30))
    return map


def globalMap_wrap(latN = 80, latS=-80):
    # draws the global map
    # map = Basemap(projection='ortho',lat_0=5,lon_0=-30,resolution='l')
    map = Basemap(projection='mill',llcrnrlat=latS,urcrnrlat=latN,llcrnrlon=-30,urcrnrlon=390,resolution='c') # a global projection centred on Greenwich
    # draw coastlines, country boundaries, fill continents.
    map.drawcoastlines(linewidth=0.25)
    map.fillcontinents(color=[.91,.91,.95],zorder=0)
    # draw the edge of the map projection region (the projection limb)
    # map.drawmapboundary(fill_color='aqua')
    # draw lat/lon grid lines every 30 degrees.
    map.drawmeridians(np.arange(-30,390,30))
    map.drawparallels(np.arange(-90,90,30))
    return map


def tropMap2():
    # draws the global map
    # map = Basemap(projection='ortho',lat_0=5,lon_0=-30,resolution='l')
    map = Basemap(projection='mill',llcrnrlat=-60,urcrnrlat=60,llcrnrlon=60,urcrnrlon=240,resolution='c') # a global projection centred on Greenwich
    # draw coastlines, country boundaries, fill continents.
    map.drawcoastlines(linewidth=0.25)
    # draw the edge of the map projection region (the projection limb)
    # map.drawmapboundary(fill_color='aqua')
    # draw lat/lon grid lines every 30 degrees.
    map.drawmeridians(np.arange(0,360,30))
    map.drawparallels(np.arange(-90,90,30))
    return map

def tropMap3():
    # draws the global map
    # map = Basemap(projection='ortho',lat_0=5,lon_0=-30,resolution='l')
    map = Basemap(projection='mill',llcrnrlat=-60,urcrnrlat=65,llcrnrlon=30,urcrnrlon=290,resolution='c') # a global projection centred on Greenwich
    # draw coastlines, country boundaries, fill continents.
    map.drawcoastlines(linewidth=0.5,color='k')
    map.fillcontinents(color=[.91,.91,.95],zorder=0)
    # draw the edge of the map projection region (the projection limb)
    # map.drawmapboundary(fill_color='aqua')
    # draw lat/lon grid lines every 30 degrees.
    map.drawmeridians(np.arange(0,360,30))
    map.drawparallels(np.arange(-90,90,30))
    return map

def tropMap5():
    # draws the global map
    # map = Basemap(projection='ortho',lat_0=5,lon_0=-30,resolution='l')
    map = Basemap(projection='mill',llcrnrlat=-10,urcrnrlat=10,llcrnrlon=30,urcrnrlon=290,resolution='c') # a global projection centred on Greenwich
    # draw coastlines, country boundaries, fill continents.
    map.drawcoastlines(linewidth=0.5,color='k')
    map.fillcontinents(color=[.91,.91,.95],zorder=0)
    # draw the edge of the map projection region (the projection limb)
    # map.drawmapboundary(fill_color='aqua')
    # draw lat/lon grid lines every 30 degrees.
    map.drawmeridians(np.arange(0,360,30))
    map.drawparallels(np.arange(-90,90,30))
    return map


def tropMap():
    # draws the global map
    # map = Basemap(projection='ortho',lat_0=5,lon_0=-30,resolution='l')
    map = Basemap(projection='mill',llcrnrlat=-40,urcrnrlat=40,llcrnrlon=80,urcrnrlon=200,resolution='c') # a global projection centred on Greenwich
    # draw coastlines, country boundaries, fill continents.
    map.drawcoastlines(linewidth=0.25)
    # draw the edge of the map projection region (the projection limb)
    # map.drawmapboundary(fill_color='aqua')
    # draw lat/lon grid lines every 30 degrees.
    map.drawmeridians(np.arange(0,360,30))
    map.drawparallels(np.arange(-90,90,30))
    return map



def shiftgrid(lon0,datain,lonsin,start=True,cyclic=360.0):
    """
    Shift global lat/lon grid east or west.

    .. tabularcolumns:: |l|L|

    ==============   ====================================================
    Arguments        Description
    ==============   ====================================================
    lon0             starting longitude for shifted grid
                     (ending longitude if start=False). lon0 must be on
                     input grid (within the range of lonsin).
    datain           original data.
    lonsin           original longitudes.
    ==============   ====================================================

    .. tabularcolumns:: |l|L|

    ==============   ====================================================
    Keywords         Description
    ==============   ====================================================
    start            if True, lon0 represents the starting longitude
                     of the new grid. if False, lon0 is the ending
                     longitude. Default True.
    cyclic           width of periodic domain (default 360)
    ==============   ====================================================

    returns ``dataout,lonsout`` (data and longitudes on shifted grid).
    """
    if np.fabs(lonsin[-1]-lonsin[0]-cyclic) > 1.e-4:
        # Use all data instead of raise ValueError, 'cyclic point not included'
        start_idx = 0
    else:
        # If cyclic, remove the duplicate point
        start_idx = 1
    if lon0 < lonsin[0] or lon0 > lonsin[-1]:
        raise ValueError, 'lon0 outside of range of lonsin'
    i0 = np.argmin(np.fabs(lonsin-lon0))
    i0_shift = len(lonsin)-i0
    if hasattr(datain,'mask'):
        dataout  = ma.zeros(datain.shape,datain.dtype)
    else:
        dataout  = np.zeros(datain.shape,datain.dtype)
    if hasattr(lonsin,'mask'):
        lonsout = ma.zeros(lonsin.shape,lonsin.dtype)
    else:
        lonsout = np.zeros(lonsin.shape,lonsin.dtype)
    if start:
        lonsout[0:i0_shift] = lonsin[i0:]
    else:
        lonsout[0:i0_shift] = lonsin[i0:]-cyclic
    dataout[:,0:i0_shift] = datain[:,i0:]
    if start:
        lonsout[i0_shift:] = lonsin[start_idx:i0+start_idx]+cyclic
    else:
        lonsout[i0_shift:] = lonsin[start_idx:i0+start_idx]
    dataout[:,i0_shift:] = datain[:,start_idx:i0+start_idx]
    return dataout,lonsout


def tropMap4():
    # draws the global map
    # map = Basemap(projection='ortho',lat_0=5,lon_0=-30,resolution='l')
    map = Basemap(projection='mill',llcrnrlat=-30,urcrnrlat=45,llcrnrlon=45,urcrnrlon=190,resolution='c') # a global projection centred on Greenwich
    # draw coastlines, country boundaries, fill continents.
    map.drawcoastlines(linewidth=0.5,color='k')
    map.fillcontinents(color=[.91,.91,.95],zorder=0)
    # draw the edge of the map projection region (the projection limb)
    # map.drawmapboundary(fill_color='aqua')
    # draw lat/lon grid lines every 30 degrees.
    map.drawmeridians(np.arange(0,360,30))
    map.drawparallels(np.arange(-90,90,30))
    return map

def tropPacMap():
    # draws the global map
    # map = Basemap(projection='ortho',lat_0=5,lon_0=-30,resolution='l')
    map = Basemap(projection='mill',llcrnrlat=-45,urcrnrlat=45,llcrnrlon=120,urcrnrlon=300,resolution='c') # a global projection centred on Greenwich
    # draw coastlines, country boundaries, fill continents.
    map.drawcoastlines(linewidth=0.5,color='k')
    map.fillcontinents(color=[.91,.91,.95],zorder=0)
    # draw the edge of the map projection region (the projection limb)
    # map.drawmapboundary(fill_color='aqua')
    # draw lat/lon grid lines every 30 degrees.
    map.drawmeridians(np.arange(0,360,30))
    map.drawparallels(np.arange(-90,90,30))
    return map

def eastTropMap():
    # draws the global map
    # map = Basemap(projection='ortho',lat_0=5,lon_0=-30,resolution='l')
    map = Basemap(projection='mill',llcrnrlat=-45,urcrnrlat=45,llcrnrlon=210,urcrnrlon=300,resolution='c') # a global projection centred on Greenwich
    # draw coastlines, country boundaries, fill continents.
    map.drawcoastlines(linewidth=0.5,color='k')
    map.fillcontinents(color=[.91,.91,.95],zorder=0)
    # draw the edge of the map projection region (the projection limb)
    # map.drawmapboundary(fill_color='aqua')
    # draw lat/lon grid lines every 30 degrees.
    map.drawmeridians(np.arange(0,360,30))
    map.drawparallels(np.arange(-90,90,30))
    return map

def eastCentTropMap():
    # draws the global map
    # map = Basemap(projection='ortho',lat_0=5,lon_0=-30,resolution='l')
    map = Basemap(projection='mill',llcrnrlat=-45,urcrnrlat=45,llcrnrlon=180,urcrnrlon=300,resolution='c') # a global projection centred on Greenwich
    # draw coastlines, country boundaries, fill continents.
    map.drawcoastlines(linewidth=0.5,color='k')
    map.fillcontinents(color=[.91,.91,.95],zorder=0)
    # draw the edge of the map projection region (the projection limb)
    # map.drawmapboundary(fill_color='aqua')
    # draw lat/lon grid lines every 30 degrees.
    map.drawmeridians(np.arange(0,360,30))
    map.drawparallels(np.arange(-90,90,30))
    return map

def IOMap():
    # draws the global map
    # map = Basemap(projection='ortho',lat_0=5,lon_0=-30,resolution='l')
    map = Basemap(projection='mill',llcrnrlat=-32,urcrnrlat=45,llcrnrlon=25,urcrnrlon=160,resolution='c') # a global projection centred on Greenwich
    # draw coastlines, country boundaries, fill continents.
    map.drawcoastlines(linewidth=0.5,color='k')
    map.fillcontinents(color=[.91,.91,.95],zorder=0)
    # draw the edge of the map projection region (the projection limb)
    # map.drawmapboundary(fill_color='aqua')
    # draw lat/lon grid lines every 30 degrees.
    map.drawmeridians(np.arange(0,360,30))
    map.drawparallels(np.arange(-90,90,30))
    return map


def tropMapLat(south,north):
    # draws the global map
    # map = Basemap(projection='ortho',lat_0=5,lon_0=-30,resolution='l')
    map = Basemap(projection='mill',llcrnrlat=south,urcrnrlat=north,llcrnrlon=30,urcrnrlon=390,resolution='c') # a global projection centred on Greenwich
    # draw coastlines, country boundaries, fill continents.
    map.drawcoastlines(linewidth=0.5,color='k')
    map.fillcontinents(color=[.91,.91,.95],zorder=0)
    # draw the edge of the map projection region (the projection limb)
    # map.drawmapboundary(fill_color='aqua')
    # draw lat/lon grid lines every 30 degrees.
    map.drawmeridians(np.arange(0,390,30))
    map.drawparallels(np.arange(-90,90,30))
    return map



def drawGlobalMap(lat,lon,field):
    
    map=globalMap()
    sstC2,lon1 = shiftgrid(330,(field[:,:]),lon,start=False,cyclic=360.0)   # orb
    lon1,lat1 = np.meshgrid(lon1,lat) # mesh the lat lon vectors
    x,y = map(lon1, lat1) # compute map proj coordinates.
#    
    c = map.pcolormesh(x,y,sstC2,cmap=brewer2mpl.get_map('RdBu', 'diverging',11,reverse=True).get_mpl_colormap(N=13)) #  do surface ebtween 0 and 10 with my colormap
    return c


def drawGlobalMap_wrap(lat,lon,field):
    
    map=globalMap_wrap()
    lat,lon,field = wrap_data_for_wrap_map(lat,lon,field)
    lon1=lon
    sstC2=field[:,:]
    lat1 = lat
    x,y = map(lon1, lat1) # compute map proj coordinates.
#    
    c = map.pcolormesh(x,y,sstC2,cmap=brewer2mpl.get_map('RdBu', 'diverging',11,reverse=True).get_mpl_colormap(N=13)) #  do surface ebtween 0 and 10 with my colormap
    return c


def drawGlobalMap_wrap_cont(lat,lon,field,conts=10,col='k'):
    
    map=globalMap_wrap()
    lat,lon,field = wrap_data_for_wrap_map(lat,lon,field)
    lon1=lon
    sstC2=field[:,:]
    lat1 = lat
    x,y = map(lon1, lat1) # compute map proj coordinates.
#    
    c = map.contour(x,y,sstC2,conts,colors=col) #  do surface ebtween 0 and 10 with my colormap
    return c


    
def drawBox(map,lat1,lon1,lat2,lon2,col=[.6,.6,1.]):
    
    x,y = map([lon1,lon1],[lat1,lat2])
    map.plot(x,y,'-',linewidth=4,color=col)

    x,y = map([lon2,lon2],[lat1,lat2])
    map.plot(x,y,'-',linewidth=4,color=col)

    x,y = map([lon1,lon2],[lat1,lat1])
    map.plot(x,y,'-',linewidth=4,color=col)

    x,y = map([lon1,lon2],[lat2,lat2])
    map.plot(x,y,'-',linewidth=4,color=col)


def wrap_data_for_wrap_map(lat1,lon1,data):
    lon1,lat1 = np.meshgrid(lon1,lat1)
    grid_dims = lat1.shape
    lat1 = np.tile(lat1,[1,3])
    lon1 = np.tile(lon1,[1,3])
    lon1[:,:grid_dims[1]] -= 360.
    lon1[:,-grid_dims[1]:] += 360.
    data=np.tile(data,[1,3])
    lat1 = lat1[:,grid_dims[1]/2:-grid_dims[1]/2]
    lon1 = lon1[:,grid_dims[1]/2:-grid_dims[1]/2]
    data = data[:,grid_dims[1]/2:-grid_dims[1]/2]
    

    return lat1,lon1,data


def map_grid(map,lat,lon):
    lon1,lat1 = np.meshgrid(lon,lat) # mesh the lat lon vectors
    x,y = map(lon1, lat1) # compute map proj coordinates.

    return x,y


def s_pole_map():

    # setup north polar stereographic basemap.
    # The longitude lon_0 is at 6-o'clock, and the
    # latitude circle boundinglat is tangent to the edge
    # of the map at lon_0. Default value of lat_ts
    # (latitude of true scale) is pole.
    map = Basemap(projection='splaea',boundinglat=-30,lon_0=30,resolution='l')
    map.drawcoastlines()
    map.fillcontinents(color=[.91,.91,.95],zorder=0)
    # draw the edge of the map projection region (the projection limb)
    # map.drawmapboundary(fill_color='aqua')
    # draw lat/lon grid lines every 30 degrees.
    map.drawmeridians(np.arange(0,360,30))
    map.drawparallels(np.arange(-180,180,20))

    return map

def s_pole_ortho():
    map = Basemap(projection='ortho',lon_0=0,lat_0=-90,resolution='c')
    map.drawcoastlines()
# draw parallels and meridians.
    map.drawparallels(np.arange(-90.,120.,30.))
    map.drawmeridians(np.arange(0.,420.,60.))
    map.fillcontinents(color=[.91,.91,.95],zorder=0)
    map.drawmapboundary(fill_color='w')
    return map


def n_pole_map():

    # setup north polar stereographic basemap.
    # The longitude lon_0 is at 6-o'clock, and the
    # latitude circle boundinglat is tangent to the edge
    # of the map at lon_0. Default value of lat_ts
    # (latitude of true scale) is pole.
    map = Basemap(projection='nplaea',boundinglat=30,lon_0=330,resolution='c')
    map.drawcoastlines()
#    map.fillcontinents(color=[.91,.91,.95],zorder=0)
    # draw the edge of the map projection region (the projection limb)
    # map.drawmapboundary(fill_color='aqua')
    # draw lat/lon grid lines every 30 degrees.
    map.drawmeridians(np.arange(0,360,30))
    map.drawparallels(np.arange(-180,180,20))

    return map


def n_am_sect():

    map = Basemap(width=12000000,height=9000000,rsphere=(6378137.00,6356752.3142),resolution='c',projection='lcc',lat_1=25.,lat_2=75,lat_0=40,lon_0=-107.,area_thresh=50000.)
    map.drawcoastlines()
    map.drawmeridians(np.arange(0,360,30))
    map.drawparallels(np.arange(-180,180,20))

    return map

def n_pac_sect():

    map = Basemap(width=12000000,height=9000000,rsphere=(6378137.00,6356752.3142),projection='lcc',lat_1=0.,lat_2=65,lat_0=40,lon_0=-170.,area_thresh=50000.)
    map.drawcoastlines()
    map.drawmeridians([120,150,210,240,270],dashes=[3,4])
    map.drawmeridians([180],dashes=[6,4])
    map.drawparallels(np.arange(-180,180,30),dashes=[3,4])
    map.drawlsmask(land_color='0.8', ocean_color='w', lsmask=None, lsmask_lons=None, lsmask_lats=None, lakes=False, resolution='c', grid=10)
    return map


def n_am_ortho():

    map = Basemap(projection='ortho',lon_0=-115,lat_0=90,area_thresh=50000.)
    map.drawcoastlines(linewidth=1,color=[.3,.9,.3])
#    map.fillcontinents(color='.9') #[.91,.91,.95]
    map.drawmeridians(np.arange(0,360,90))
    map.drawparallels(np.arange(-180,180,30))
#    map.drawmapboundary(fill_color='w')
    map.drawlsmask(land_color='0.8', ocean_color='w', lsmask=None, lsmask_lons=None, lsmask_lats=None, lakes=False, resolution='c', grid=10)

    return map


def n_pac_sect_2():

    map = Basemap(width=16000000,height=9000000,rsphere=(6378137.00,6356752.3142),projection='lcc',lat_1=0.,lat_2=65,lat_0=30,lon_0=-145.,area_thresh=50000.)
    map.drawcoastlines()
    map.drawmeridians([120,150,210,240,270],dashes=[3,4])
    map.drawmeridians([180],dashes=[6,4])
    map.drawparallels(np.arange(-180,180,30),dashes=[3,4])
    map.drawlsmask(land_color='0.8', ocean_color='w', lsmask=None, lsmask_lons=None, lsmask_lats=None, lakes=False, resolution='c', grid=10)
    return map

def n_pac_sect_2_w():

    map = Basemap(width=16000000,height=9000000,rsphere=(6378137.00,6356752.3142),projection='lcc',lat_1=0.,lat_2=65,lat_0=30,lon_0=-190.,area_thresh=50000.)
    map.drawcoastlines()
    map.drawmeridians([120,150,210,240,270],dashes=[3,4])
    map.drawmeridians([180],dashes=[6,4])
    map.drawparallels(np.arange(-180,180,30),dashes=[3,4])
    map.drawlsmask(land_color='0.8', ocean_color='w', lsmask=None, lsmask_lons=None, lsmask_lats=None, lakes=False, resolution='c', grid=10)
    return map








def n_pac_ortho():

#    map = Basemap(projection='nsper',lon_0=200,lat_0=20,resolution='c',satellite_height=248e6)#,area_thresh=50000.)
    map = Basemap(projection='hammer',lon_0=200,lat_0=20,resolution='c')#,area_thresh=50000.)

    map.drawcoastlines(linewidth=2.5,color=[.8,.8,.8])
#    map.fillcontinents(color='b',lake_color = 'w') #[.91,.91,.95]
    map.drawmeridians(np.arange(0,360,30))
    map.drawparallels(np.arange(-180,180,20))
    map.drawmapboundary(fill_color='white')
    return map

