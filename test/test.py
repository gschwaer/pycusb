from typing import Optional
import pytest
import pytest_mock
import cusb

write_read_map: dict[bytes, bytes] = {}


class SerialMock:
    def __init__(self, path: str, timeout: int):
        self._last_write: Optional[bytes] = None

    def write(self, data: bytes):
        assert data.endswith(b"\r")
        data_len = len(data)
        data = data.rstrip(b"\r")
        print(f"Wrote: {data!r}")
        self._last_write = data
        return data_len

    def read_all(self) -> bytes:
        # We only use this to clean up the buffer, so the result is always discarded.
        return b""

    def read_until(self) -> bytes:
        assert self._last_write
        input = write_read_map.get(self._last_write, b"")
        print(f"Read: {input!r}")
        return input + b"\r\n"

    def close(self):
        pass


def set_write_read_map(map: dict[bytes, bytes]):
    global write_read_map
    write_read_map = map


@pytest.fixture
def cusb_mock(mocker: pytest_mock.MockerFixture):
    mocker.patch("serial.Serial", new=SerialMock)
    return cusb.CUsb("__don't_care__")


def test_port_power_on_while_port_power_is_on(cusb_mock: cusb.CUsb):
    set_write_read_map(
        {
            b"?Q": b"CENTOS000104v04",
            b"GP": b"FFFFFFFF",
        }
    )
    with cusb_mock as hub:
        hub.port_power_on(1, True)


# set_ports_0_3.log
def test_port_power_off_while_port_power_is_on(cusb_mock: cusb.CUsb):
    set_write_read_map(
        {
            b"?Q": b"CENTOS000104v04",
            b"GP": b"FEFFFFFF",
            b"SPpass    FAFFFFFF": b"GFAFFFFFF",
        }
    )
    with cusb_mock as hub:
        hub.port_power_on(3, True)


# set_ports_0_3.log2
def test_port_power_off_while_port_power_is_on2(cusb_mock: cusb.CUsb):
    set_write_read_map(
        {
            b"?Q": b"CENTOS000104v04",
            b"GP": b"FEFFFFFF",
            b"SPpass    FAFFFFFF": b"GFAFFFFFF",
        }
    )
    with cusb_mock as hub:
        hub.port_power_on(3, True)


# get_ports.log
def test_port_power_is_on(cusb_mock: cusb.CUsb):
    set_write_read_map(
        {
            b"?Q": b"CENTOS000104v04",
            b"GP": b"FBFFFFFF",
            b"GP": b"FBFFFFFF",
            b"GP": b"FBFFFFFF",
            b"GP": b"FBFFFFFF",
        }
    )
    with cusb_mock as hub:
        assert hub.port_power_is_on(1)
        assert hub.port_power_is_on(2)
        assert not hub.port_power_is_on(3)
        assert hub.port_power_is_on(4)


# save_port_states.log
def test_save_port_states(cusb_mock: cusb.CUsb):
    set_write_read_map(
        {
            b"?Q": b"CENTOS000104v04",
            b"WPpass    ": b"G",
        }
    )
    with cusb_mock as hub:
        hub.save_current_state_as_default()


# factory_reset.log
def test_factory_reset(cusb_mock: cusb.CUsb):
    set_write_read_map(
        {
            b"?Q": b"CENTOS000104v04",
            b"RDpass    ": b"G",
        }
    )
    with cusb_mock as hub:
        hub.factory_reset()


# reset.log
def test_reset(cusb_mock: cusb.CUsb):
    set_write_read_map(
        {
            b"?Q": b"CENTOS000104v04",
            b"RHpass    ": b"",
        }
    )
    with cusb_mock as hub:
        hub.reset()
