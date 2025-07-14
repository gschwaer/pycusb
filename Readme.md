# pycusb

A python library for managed USB hubs that are usually operated by a command line tool called cusbi
(Linux Intel), cusba (Linux Arm), cusbm (Mac), or CUSBC/CUSBCTL (Windows), e.g., hubs from the
companies EXSYS and StarTech.

## Usage

### as library

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

### as CLI tool

```bash
$ pycusb --help
CUSB Hub Control

Usage:
  pycusb set <port> (on|off) PATH
  pycusb get <port> PATH
  pycusb save PATH
  pycusb reset PATH
  pycusb factory_reset PATH
  pycusb -h | --help

Arguments:
  PATH          Path to serial device file controlling the hub.

Options:
  -h --help     Show this help message.
```

Example: switch off port 1 for 1 second

```bash
pycusb set 1 off /dev/serial/by-id/usb-FTDI_FT232R_USB_UART_B0036Y2H-if00-port0
sleep 1
pycusb set 1 on /dev/serial/by-id/usb-FTDI_FT232R_USB_UART_B0036Y2H-if00-port0
```

## Installation

### as library

Add `pycusb` to your `pyproject.toml`:

```toml
[project]
dependencies = [
    "pycusb",
]
```

### as CLI tool

Create and activate a virtual environment, then run

```bash
pip install pycusb
```

## Development

Clone the repo, create and activate a virtual environment, then install dependencies with:

```bash
pip install -e '.[dev]'
```

Test with

```bash
pytest test/test.py
```
