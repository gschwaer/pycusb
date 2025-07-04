# pycusb

A python library for managed USB hubs that are usually operated by a command line tool called cusbi
(Linux Intel), cusba (Linux Arm), cusbm (Mac), or CUSBC/CUSBCTL (Windows), e.g., hubs from the
companies EXSYS and StarTech.

## Usage

```python
from cusb import CUsb
import time

# Example:
path_to_device = "/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_B0036Y2H-if00-port0"
port = 1

with CUsb(path_to_device) as hub:
    hub.port_power_on(port, False)
    time.sleep(1)
    hub.port_power_on(port, True)
```
