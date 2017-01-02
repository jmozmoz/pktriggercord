<<<<<<< HEAD
from __future__ import print_function

import sys
import os
import time
import pktriggercord
import ctypes

print('debug:', pktriggercord.debug)
pktriggercord.debug = ctypes.c_ubyte(1)
print('debug:', pktriggercord.debug)

model = None
device = None
timeout = ctypes.c_int(2)
buf = pktriggercord.String((ctypes.c_char*2100)())

camhandle = pktriggercord.camera_connect( model, device, timeout, buf)

camera_name = pktriggercord.pslr_camera_name(camhandle);
print("camera:", camera_name)

bufsize = pktriggercord.pslr_get_model_buffer_size( camhandle );
print("bufsize:", bufsize)
status_buffer = (ctypes.c_uint * pktriggercord.MAX_STATUS_BUF_SIZE)()
pktriggercord.pslr_get_status_buffer(camhandle, status_buffer)
pktriggercord.hexdump(status_buffer, bufsize if bufsize > 0 else pktriggercord.MAX_STATUS_BUF_SIZE)
sys.stdout.flush()

status = pktriggercord.pslr_status()
status_ptr = ctypes.cast(ctypes.addressof(status), ctypes.POINTER(pktriggercord.pslr_status))
pktriggercord.pslr_get_status(camhandle, status_ptr);
print(status)
print(pktriggercord.collect_status_info(camhandle, status).data.decode())

pktriggercord.camera_close(camhandle)
print('closed camera')
=======
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
>>>>>>> branch 'python_wrapper' of https://github.com/jmozmoz/pktriggercord.git
