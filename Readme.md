# pycusb

A python library for managed USB hubs that are usually operated by a command line tool called cusbi
(Linux Intel), cusba (Linux Arm), cusbm (Mac), or CUSBC/CUSBCTL (Windows), e.g., hubs from the
companies EXSYS and StarTech.

## Usage

### Usage as library

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

### Usage as CLI tool

```text
$ pycusb --help
CUSB Hub Control

This CLI tool is able to *set* or *get* the state of the managed USB hub. It
can *save* the current state as the default, so after a power loss, this state
will be restored. The hub can also be *reset*, or a *factory reset* can be
issued, resetting any stored state and/or set password.

If a password is required, it can be provided to all commands as an option. By
default the implementation uses "pass", which is the factory default. The *get*
command does not need the password to succeed.

Usage:
  pycusb [options] get <port> PATH
  pycusb [options] set <port> (on|off) PATH
  pycusb [options] save PATH
  pycusb [options] reset PATH
  pycusb [options] factory_reset PATH
  pycusb -h | --help

Arguments:
  PATH                      Path to serial device file controlling the hub.

Options:
  -p --password=<password>  Show this help message [default: pass].
```

Example: switch off port 1 for 1 second

```text
pycusb set 1 off /dev/serial/by-id/usb-FTDI_FT232R_USB_UART_B0036Y2H-if00-port0
sleep 1
pycusb set 1 on /dev/serial/by-id/usb-FTDI_FT232R_USB_UART_B0036Y2H-if00-port0
```

## Installation

### Installation as library

Add `pycusb` to your `pyproject.toml`:

```toml
[project]
dependencies = [
    "pycusb",
]
```

### Installation as CLI tool

Create and activate a virtual environment, then run

```text
pip install pycusb
```

## Development

Clone the repo, create and activate a virtual environment, then install dependencies with:

```text
pip install -e '.[dev]'
```

Test with

```text
pytest test/test.py
```
