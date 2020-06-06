import freenect
import numpy as np
from matplotlib import pyplot as plt
from datetime import datetime

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
    time = now.strftime("%H%M%S")
    date = now.strftime("%m%d%Y")
    return "%s_%s.png" % (time, date)

def nir(outdir=None, color_map='Spectral'):
    # init_kinect('on')
    ir = freenect.sync_get_video(0, freenect.VIDEO_IR_10BIT)
    # init_kinect('off')
    plt.imshow(ir[0], color_map)
    freenect.sync_stop()
    if outdir:
        timeDate = get_time()
        fileName = 'nir_%s' % timeDate
        out = '%s/%s' % (outdir, fileName)
        plt.savefig(out, bbox_inches='tight')
    else:
        return ir[0]

def rgb(outdir=None):
    # init_kinect('on')
    rgb = freenect.sync_get_video(0, freenect.VIDEO_RGB)
    # init_kinect('off')
    if outdir:
        plt.imshow(rgb[0])
        timeDate = get_time()
        fileName = 'rgb_%s' % timeDate
        out = '%s/%s' % (outdir, fileName)
        plt.savefig(out, bbox_inches='tight')
    else:
        return rgb[0]

def get_band(arr, band):
    out_arr = []
    for i in range(arr[0]):
        for j in range(arr[1]):
            out_arr.append(arr[i][j][band])
    outArr = out_arr.reshape(arr.shape)

