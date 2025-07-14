"""CUSB Hub Control

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
"""

# import argparse
from typing import Any
import cusb

# from pathlib import Path
from docopt import docopt


def main() -> None:
    assert __doc__
    args: dict[str, Any] = docopt(
        __doc__,
    )

    if args["set"]:
        port_str = args["<port>"]
        assert port_str and int(port_str) >= 1, "Invalid port"
        port = int(port_str)

        action = "on" if args["on"] else "off"

        path = args["PATH"]
        assert path and isinstance(path, str)

        with cusb.CUsb(path) as hub:
            print(f"Switching port {port} {action}")
            hub.port_power_on(port, action == "on")
    elif args["get"]:
        port_str = args["<port>"]
        assert port_str and int(port_str) >= 1, "Invalid port"
        port = int(port_str)

        path = args["PATH"]
        assert path and isinstance(path, str)

        with cusb.CUsb(path) as hub:
            state = "on" if hub.port_power_is_on(port) else "off"
            print(f"Port {port}={state}")
    elif args["save"]:
        path = args["PATH"]
        assert path and isinstance(path, str)

        with cusb.CUsb(path) as hub:
            print(f"Saving current state as default.")
            hub.save_current_state_as_default()
    elif args["reset"]:
        path = args["PATH"]
        assert path and isinstance(path, str)

        with cusb.CUsb(path) as hub:
            print(f"Resetting hub.")
            hub.reset()
    elif args["factory_reset"]:
        path = args["PATH"]
        assert path and isinstance(path, str)

        with cusb.CUsb(path) as hub:
            print(f"Resetting hub to factory defaults.")
            hub.factory_reset()

if __name__ == "__main__":
    main()
