#!/usr/bin/env python

import os
from datetime import datetime
import numpy as np

#import astropy.io.fits as pyfits
from astropy.time import Time, TimeDelta


MJDREFI = 59945                  # 2023-01-01T00:00:00 
MJDREFF = 0.0008007407377590425  # fraction of day (in TT)
MJDREF = MJDREFI + MJDREFF

def astime2mstime(astime) :
    return mjdtt2mstime(astime.tt.mjd)

def mjdutc2mstime(mjdutc) :
    mjdtt = Time(mjdutc, format='mjd', scale='utc').tt.mjd
    return mjdtt2mstime(mjdtt)
    
def mjdtt2mstime(mjdtt) :
    return (mjdtt - MJDREF)*86400.
    
def mstime2astime(mstime) :
    return Time(mstime/86400.+MJDREF, format='mjd', scale='tt') 


if __name__=="__main__" :

    vastime1 = Time(datetime(2024,1,1,0,0,0), scale='utc') + TimeDelta(1,scale='tt',format='sec')*np.linspace(0,10,11)
    print("MJD(TT)=", vastime1.tt.mjd)
    vmstime1 = astime2mstime(vastime1)
    print("Mission time=", vmstime1)
    
    vastime2 = Time(datetime(2024,1,1,0,0,0), scale='tt') + TimeDelta(1,scale='tt',format='sec')*np.linspace(0,10,11)
    print("MJD(TT)=", vastime2.tt.mjd)
    vmstime2 = astime2mstime(vastime2)
    print("Mission time=", vmstime2)
    


