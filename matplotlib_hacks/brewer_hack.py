def brewer_hack(nm = 'RdBu', typ = 'diverging',N=11,rev=True,cmap_name='newcmap'):
    '''
    def brewer_hack(nm = 'RdBu', typ = 'diverging',N=11,rev=True,cmap_name='newcmap'):
'''

    import brewer2mpl
    import matplotlib as mpl

    N_brewer = N

    if N > 11:
        N_brewer = 11

    junk = brewer2mpl.get_map(nm,typ,N_brewer,reverse=rev)
    junk1  = junk.mpl_colors[:N_brewer/2]
    junk1.append(junk.mpl_colors[N_brewer/2])
    [junk1.append(i) for i in junk.mpl_colors[N_brewer/2:] ]
    newcmap = mpl.colors.LinearSegmentedColormap.from_list(cmap_name,junk1,N=N+1)
    mpl.cm.register_cmap(cmap=newcmap)

    return newcmap
    
    
