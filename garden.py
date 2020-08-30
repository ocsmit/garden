#!/usr/bin/env

import freenect
import numpy as np
from matplotlib import pyplot as plt
from datetime import datetime
from PIL import Image

out_dir = "/home/pi/garden/results"

class Garden:
    def __init__(self):
        '''
        Function to initialize kinect and remove connection to kinect when finished
        processing.

        *args:
            'on'
            'off'
        '''
        init = freenect.init()
        self.kinect = freenect.open_device(init, 0)
        self.status = 1

    def switch(self):
        freenect.close_device(self.kinect)
        #freenect.shutdown(self.kinect)
        self.status = 0

    def depth_switch(self, *args):
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

    def get_time(self):
        '''
        Function to get time and date and format a tif file name.
        '''
        now = datetime.now()
        time = now.strftime("%H%M")
        date = now.strftime("%m%d%Y")
        return "%s_%s.tif" % (time, date)



    def nir(self, outdir):
        '''
        Function to take NIR band picture.
        '''
        ir = freenect.sync_get_video(0, freenect.VIDEO_IR_8BIT)
        # freenect.sync_stop()

        timeDate = self.get_time()
        fileName = 'ir_%s' % timeDate
        out = '%s/%s' % (outdir, fileName)

        img = Image.fromarray(ir[0])
        img.save(out)
        freenect.sync_stop()

        print('IR Saved')

    def rgb(self, outdir):
        '''
        Function to take RGB picture.
        '''
        rgb = freenect.sync_get_video(0, freenect.VIDEO_RGB)

        timeDate = get_time()
        fileName = 'red_%s' % timeDate
        out = '%s/%s' % (outdir, fileName)

        red = rgb[0]

        img = Image.fromarray(red[:,:,0])
        img.save(out)
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

