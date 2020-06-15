#!/usr/bin/env

import freenect
import numpy as np
from matplotlib import pyplot as plt
from datetime import datetime
from PIL import Image

out_dir = "/home/pi/garden_out"

def init_kinect(*args):
    if args == 'on':
        context = freenect.init()
        kinect = freenect.open_device(context, 0)
    if args == 'off':
        freenect.close_device(kinect)
        freenect.shutdown(kinect)

def depth_switch(*args):
    if args == 'on':
        freenect.start_depth(depthSensor)
    if args == 'off':
        freenect.stop_depth(depthSensor)

def get_time():
    now = datetime.now()
    time = now.strftime("%H%M")
    date = now.strftime("%m%d%Y")
    return "%s_%s.png" % (time, date)

def nir(outdir=None, color_map='Spectral'):
    ir = freenect.sync_get_video(0, freenect.VIDEO_IR_10BIT)
    freenect.sync_stop()

    timeDate = get_time()
    fileName = 'nir_%s' % timeDate
    out = '%s/%s' % (outdir, fileName)

    plt.imsave(out, ir[0], format='png')

def rgb(outdir=None):
    rgb = freenect.sync_get_video(0, freenect.VIDEO_RGB)
    freenect.sync_stop()

    timeDate = get_time()
    fileName = 'rgb_%s' % timeDate
    out = '%s/%s' % (outdir, fileName)

    plt.imsave(out, rgb[0], format='png')

def get_band(arr, band):
    out_arr = []
    for i in range(arr[0]):
        for j in range(arr[1]):
            out_arr.append(arr[i][j][band])
    outArr = out_arr.reshape(arr.shape)

if __name__ == "__main__":
    init_kinect('on')
    rgb(outdir=out_dir)
    nir(outdir=out_dir)
    init_kinect('off')
