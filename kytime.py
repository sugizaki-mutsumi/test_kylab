#!/usr/bin/env python

import sys
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

def print_usage() :
    print("(Usage) kytime.py (utc/tt/jd(utc)/mjd(utc)/gps/mission(koyoh)) (time)")

    
if __name__=="__main__" :

    inp_ok = False ### default

    if len(sys.argv)==3 :
        inp1 = sys.argv[1]
        inp2 = sys.argv[2]

        if inp1=="utc" :
            t = Time(inp2, format='isot', scale='utc')
            inp_ok = True
        elif inp1=="tt" :
            t = Time(inp2, format='isot', scale='tt')
            inp_ok = True
        elif inp1=="jd" :
            t = Time(inp2, format='jd', scale='utc')
            inp_ok = True
        elif inp1=="mjd" :
            t = Time(inp2, format='mjd', scale='utc')
            inp_ok = True
        elif inp1=="gps" :
            t = Time(float(inp2), format='gps')
            inp_ok = True
        elif inp1=="mission" or inp1=='koyoh' :
            t = mstime2astime(float(inp2))
            inp_ok = True
        else :
            inp_ok = False

    if inp_ok :
        print("Time(UTC) = ", t.utc.fits)
        print("Time(TT)  = ", t.tt.fits)
        print("JD(UTC)   = ", t.utc.jd)
        print("MJD(UTC)  = ", t.utc.mjd)
        print("GPS_time  = ", t.gps)
        mstime = astime2mstime(t)
        print("Mission(KOYOH) =", mstime)
    else :
        print_usage()
        
    
    #vastime1 = Time(datetime(2024,1,1,0,0,0), scale='utc') + TimeDelta(1,scale='tt',format='sec')*np.linspace(0,10,11)
    #print("MJD(TT)=", vastime1.tt.mjd)
    #vmstime1 = astime2mstime(vastime1)
    #print("Mission time=", vmstime1)
    
    #vastime2 = Time(datetime(2024,1,1,0,0,0), scale='tt') + TimeDelta(1,scale='tt',format='sec')*np.linspace(0,10,11)
    #print("MJD(TT)=", vastime2.tt.mjd)
    #vmstime2 = astime2mstime(vastime2)
    #print("Mission time=", vmstime2)
    


