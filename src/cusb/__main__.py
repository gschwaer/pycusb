import argparse
import cusb


def main():
    parser = argparse.ArgumentParser(
        prog="cusb", description="Control a cusb managed USB hub"
    )
    parser.add_argument("path_to_serial_device")
    parser.add_argument(
        "-p", "--port", help="Port number starting from 1", required=True
    )
    parser.add_argument("-a", "--action", help="One of: on, off", required=True)

    args = parser.parse_args()
    dev = args.path_to_serial_device

    assert args.action == "on" or args.action == "off", "Invalid action"
    action = args.action

    assert args.port is not None and int(args.port) >= 1, "Invalid port"
    port = int(args.port)

    with cusb.CUsb(dev) as hub:
        print(f"Switching port {port} {action}")
        hub.port_power_on(port, action == "on")


main()
