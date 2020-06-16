#!/usr/bin/env

import freenect
import numpy as np
from matplotlib import pyplot as plt
from datetime import datetime
from PIL import Image

out_dir = "/home/pi/garden/results"

def init_kinect(*args):
    '''
    Function to initialize kinect and remove connection to kinect when finished
    processing.

    *args:
            'on'
            'off'
    '''
    if args == 'on':
        context = freenect.init()
        kinect = freenect.open_device(context, 0)
    if args == 'off':
        freenect.close_device(kinect)
        freenect.shutdown(kinect)

def depth_switch(*args):
    '''
    function to switch depth sensor on or off.

    *args:
            'on'
            'off'

    '''
    if args == 'on':
        freenect.start_depth(depthSensor)
    if args == 'off':
        freenect.stop_depth(depthSensor)

def get_time():
    '''
    Function to get time and date and format a png file name.
    '''
    now = datetime.now()
    time = now.strftime("%H%M")
    date = now.strftime("%m%d%Y")
    return "%s_%s.tif" % (time, date)

def nir(outdir):
    '''
    Function to take NIR band picture.
    '''
    ir = freenect.sync_get_video(0, freenect.VIDEO_IR_8BIT)
    # freenect.sync_stop()

    timeDate = get_time()
    fileName = 'ir_%s' % timeDate
    out = '%s/%s' % (outdir, fileName)

    img = Image.fromarray(ir[0])
    img.save(out)
    freenect.sync_stop()

    print('IR Saved')

def rgb(outdir):
    '''
    Function to take RGB picture.
    '''
    rgb = freenect.sync_get_video(0, freenect.VIDEO_RGB)

    timeDate = get_time()
    fileName = 'red_%s' % timeDate
    out = '%s/%s' % (outdir, fileName)

    img = Image.fromarray(rgb[0])
    img.save(out)
    #plt.imsave(out, full_img[:,:,0], format='png')
    freenect.sync_stop()

    print('Red Band saved')

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

