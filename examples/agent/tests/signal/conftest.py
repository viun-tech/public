import socket
import threading
import time

import pytest
from pymodbus.client import ModbusTcpClient
from pymodbus.datastore import (
    ModbusSequentialDataBlock,
    ModbusServerContext,
    ModbusSlaveContext,
)
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.server.async_io import ServerStop, StartTcpServer


@pytest.fixture(scope="module")
def modbus_server_port():
    """
    Returns a random port number that is not in use.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("localhost", 0))
        return s.getsockname()[1]


@pytest.fixture(scope="module")
def modbus_server(modbus_server_port):
    store = ModbusSlaveContext(
        di=ModbusSequentialDataBlock(0, [17] * 100),
        co=ModbusSequentialDataBlock(0, [0] * 100),  # Initialize coils to False
        hr=ModbusSequentialDataBlock(0, [17] * 100),
        ir=ModbusSequentialDataBlock(0, [17] * 100),
    )

    context = ModbusServerContext(slaves=store, single=True)

    identity = ModbusDeviceIdentification()

    # the actual server is started in a new thread
    def run_server():
        StartTcpServer(
            context=context,
            identity=identity,
            address=("localhost", modbus_server_port),
        )

    thread = threading.Thread(target=run_server)
    thread.start()

    # poll until the server is up
    max_retries = 10
    retries = 0
    server_started = False
    while retries < max_retries and not server_started:
        try:
            with socket.create_connection(("localhost", modbus_server_port), timeout=1):
                server_started = True
        except ConnectionRefusedError:
            time.sleep(0.5)
            retries += 1

    if not server_started:
        raise RuntimeError("Modbus server did not start in the expected time.")

    yield

    ServerStop()


@pytest.fixture(scope="function")
def modbus_client(modbus_server_port):
    client = ModbusTcpClient("localhost", port=modbus_server_port)
    yield client
    client.close()


@pytest.fixture(scope="function")
def reset_coils_after_test(modbus_client):
    yield
    modbus_client.write_coils(0, [False] * 99)
