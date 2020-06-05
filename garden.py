import freenect
import numpy as np
from matplotlib import pyplot as plt

def save_ir_plot(out_plot=None, color_map='Spectral'):
    ir = freenect.sync_get_video(0, freenect.VIDEO_IR_10BIT)
    plt.imshow(ir[0], color_map)
    if out_plot:
        plt.savefig(out_plot, bbox_inches='tight')
    else:
        return ir[0]

def rgb(out_plot=None):
    rgb = freenect.sync_get_video(0, freenect.VIDEO_RGB)
    plt.imshow(rgb[0])
    if out_plot:
        plt.savefig(out_plot, bbox_inches='tight')
    else:
        return rgb[0]
