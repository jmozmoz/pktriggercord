import sys
import os
import time
import pktriggercord
import ctypes

pktriggercord.debug = True

model = None
device = None
timeout = 0

buf = pktriggercord.String((ctypes.c_char*2100)())

camhandle = pktriggercord.camera_connect( model, device, timeout, buf)

camera_name = pktriggercord.pslr_camera_name(camhandle);
print(camera_name)

# time.sleep(1)

pktriggercord.camera_close(camhandle)
