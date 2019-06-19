from numpy import array, logical_and

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

    xmin = x.min()
    ymin = y.min()
    zmin = z.min()

    zblk = (z.max()-zmin)/N
    xblk = (x.max()-xmin)/nx
    yblk = (y.max()-ymin)/ny

    Z = array([' ']*nx*ny)
    for i in range(nx):
        for j in range(ny):
            x0 = xmin + i*xblk
            y0 = ymin + j*yblk
            x1 = xmin + (i+1)*xblk
            y1 = ymin + (j+1)*yblk
            
            idxx = logical_and(x0 < x, x < x1)
            idxy = logical_and(y0 < y, y < y1)
            idx = logical_and(idxx,idxy)
            if not idx.any():
                Z[i+j*nx] = empty
            else:
                Zval = z[idx].mean()
                idxz = ((Zval - zmin)/zblk).astype('int64')
                Z[i+j*nx] = symbs[idxz]
    Z = ''.join(Z)
    Z = [Z[i:i+nx] for i in range(0,nx*ny,nx)]
    Z.reverse()
    for i in range(ny):
        print(Z[i])


