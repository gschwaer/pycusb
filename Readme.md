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
pip install git+https://github.com/gschwaer/pycusb.git
```

## Development

Clone repo, create and activate a virtual environment, then install dependencies with:

```bash
pip install -e '.[dev]'
```

Test with

```bash
pytest test/test.py
```
