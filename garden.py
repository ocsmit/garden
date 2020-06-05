import freenect
import numpy as np
from matplotlib import pyplot

def save_ir_plot(out_plot=None):
    ir = freenect.sync_get_video(0, freenect.VIDEO_IR_10BIT)
    plt.imshow(ir[0])
    if out_plot:
        plt.savefig(out_plot)
    else:
        return ir[0]

