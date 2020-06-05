import freenect
import numpy as np
from matplotlib import pyplot as plt
from datetime import datetime


def get_time():
    now = datetime.now()
    time = now.strftime("%H%M%S")
    date = now.strftime("%m%d%Y")
    return "%s_%s.png" % (time, date)

def nir(outdir=None, color_map='Spectral'):
    ir = freenect.sync_get_video(0, freenect.VIDEO_IR_10BIT)
    plt.imshow(ir[0], color_map)
    if outdir:
        timeDate = get_time()
        fileName = 'nir_%s' % timeDate
        out = '%s/%s' % (outdir, fileName)
        plt.savefig(out, bbox_inches='tight')
    else:
        return ir[0]

def rgb(outdir=None):
    rgb = freenect.sync_get_video(0, freenect.VIDEO_RGB)
    plt.imshow(rgb[0])
    if outdir:
        timeDate = get_time()
        fileName = 'rgb_%s' % timeDate
        out = '%s/%s' % (outdir, fileName)
        plt.savefig(out, bbox_inches='tight')
    else:
        return rgb[0]
