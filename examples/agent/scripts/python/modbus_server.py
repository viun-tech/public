#!/usr/bin/env python3
"""
Modbus Server Script

This script initializes and runs a Modbus TCP server on the specified port on localhost.
The server contains Discrete Inputs, Coils, Input Registers, and Holding Registers, each initialized with a specific value.

Usage: modbus_server.py [OPTIONS]

Options:
  -p, --port INTEGER  Modbus server port (default: 502)
  --help              Show this message and exit.

Server Initialization:
    - Discrete Inputs: Initialized with value 17 for the first 100 addresses.
    - Coils: Initialized with value 0 (False) for the first 100 addresses.
    - Input Registers: Initialized with value 17 for the first 100 addresses.
    - Holding Registers: Initialized with value 17 for the first 100 addresses.

Dependencies:
    - pymodbus

Logging:
    Basic logging is set up, capturing events of INFO and higher levels. Log messages are printed to the console.

Exit:
    The script can be interrupted using Ctrl+C or sending a KeyboardInterrupt, which will also stop the Modbus server.

Note:
    Ensure no other processes are using the specified port before starting the Modbus server.
"""
import logging
import socket
import threading
import time

import click
from pymodbus.datastore import (
    ModbusSequentialDataBlock,
    ModbusServerContext,
    ModbusSlaveContext,
)
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.server.async_io import ServerStop, StartTcpServer

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

run_server_thread = True


@click.command()
@click.option("-p", "--port", default=502, help="Modbus server port (default: 502)")
def start_server(port: int):
    global run_server_thread
    try:
        logger.info(f"Starting modbus server on port {port}")

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
                address=("0.0.0.0", port),
            )

        thread = threading.Thread(target=run_server, daemon=True)
        thread.start()

        # poll until the server is up
        max_retries = 10
        retries = 0
        server_started = False
        while retries < max_retries and not server_started:
            try:
                with socket.create_connection(("localhost", port), timeout=1):
                    server_started = True
            except ConnectionRefusedError:
                time.sleep(0.5)
                retries += 1

        if not server_started:
            raise RuntimeError("Modbus server did not start in the expected time.")

        logger.info(f"Modbus server started on port {port}")

        while run_server_thread:
            time.sleep(1)
    finally:
        ServerStop()


if __name__ == "__main__":
    try:
        start_server()

    except KeyboardInterrupt:
        logger.info("Received keyboard interrupt. Shutting down...")
        run_server_thread = False
