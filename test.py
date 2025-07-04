from cusb import CUsb
import time

# Example:
path_to_device = "/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_B0036Y2H-if00-port0"
port = 2

with CUsb(path_to_device) as hub:
    hub.port_power_on(port, False)
    time.sleep(1)
    hub.port_power_on(port, True)
