import numpy as np

__all__ = ['contours']

def contours(x,y,z,nx,ny,levels=None):
    """ Simple ascii-based contour plotter
    Parameters:
        x,  x-coordinates
        y,  y-coordinates
        z,  z-coordinates
        nx, x-resolution, *for my terminal a ratio of about 2.11*ny is about equal axes*
        ny, y-resolution
        levels, (default: 15), # of different z-value groupings
    """
    empty = ' '
    symbols = ['\'','.','"',':','&','(','/','x','\\',')','%','#','O','@','$']
    ns = len(symbols)
    N = len(symbs) if levels is None else levels
    symbs = symbols if levels is None else symbols[0:ns:int(ns/N)]

    zblk = (z.max()-z.min())/N
    xblk = (x.max()-x.min())/nx
    yblk = (y.max()-y.min())/ny

    Z = np.array([' ']*nx*ny)
    for i in range(nx):
        for j in range(ny):
            x0 = x.min() + i*xblk
            y0 = y.min() + j*yblk
            x1 = x.min() + (i+1)*xblk
            y1 = y.min() + (j+1)*yblk
            
            idxx = np.logical_and(x0 < x, x < x1)
            idxy = np.logical_and(y0 < y, y < y1)
            idx = np.logical_and(idxx,idxy)
            if not idx.any():
                Z[i+j*nx] = empty
            else:
                Zval = z[idx].mean()
                idxz = np.floor((Zval - z.min())/zblk).astype('int64')
                Z[i+j*nx] = symbs[idxz]
    Z = ''.join(Z)
    Z = [Z[i:i+nx] for i in range(0,len(Z),nx)]
    Z.reverse()
    for i in range(len(Z)):
        print(Z[i])


