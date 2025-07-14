"""CUSB Hub Control

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

    password = args["--password"]
    port = None
    if args["<port>"]:
        port = int(args["<port>"])
        assert port >= 1, "Invalid port (port numbers start at 1)"
    path = args["PATH"]
    assert path and isinstance(path, str)
    action = None
    if args["on"] or args["off"]:
        assert args["on"] and not args["off"] or not args["on"] and args["off"]
        action = args["on"]

    with cusb.CUsb(path, password=password) as hub:

        if args["set"]:
            assert port is not None
            assert action is not None

            action_str = "on" if action else "off"
            print(f"Switching port {port} {action_str}")
            hub.port_power_on(port, action)

        elif args["get"]:
            assert port is not None

            state = "on" if hub.port_power_is_on(port) else "off"
            print(f"Port {port}={state}")

        elif args["save"]:
            print(f"Saving current state as default.")
            hub.save_current_state_as_default()

        elif args["reset"]:
            print(f"Resetting hub.")
            hub.reset()

        elif args["factory_reset"]:
            print(f"Resetting hub to factory defaults.")
            hub.factory_reset()

if __name__ == "__main__":
    main()
