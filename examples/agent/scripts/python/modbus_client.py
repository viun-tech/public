#!/usr/bin/env python3
"""
Modbus Client Script

This script provides an interface for interacting with a Modbus server running on localhost.
It allows the user to write values to specific coils of the Modbus server.

Usage: modbus_client.py [OPTIONS]

Options:
  -p, --port INTEGER  Modbus server port (default: 502)
  -h, --host TEXT     Modbus server host (default: localhost)
  --help              Show this message and exit.

User input format:
    Please enter 'coil number, value' (e.g '1,True')
    - 'coil number' is the coil's address you want to write to. It must be a number.
    - 'value' is the desired value for the coil. It can be either 'True' or 'False'.

Dependencies:
    - pymodbus

Logging:
    Basic logging is set up, capturing events of INFO and higher levels. Log messages are printed to the console.

Exit:
    The script can be interrupted using Ctrl+C or sending a KeyboardInterrupt.

Note:
    Ensure that a Modbus server is running on localhost and the specified port before using this client.
"""
import logging

import click
from pymodbus.client import ModbusTcpClient

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


@click.command()
@click.option("-p", "--port", default=502, help="Modbus server port (default: 502)")
@click.option(
    "-h", "--host", default="localhost", help="Modbus server host (default: localhost)"
)
def main(host: str, port: int):
    try:
        client = ModbusTcpClient(host, port=port)

        while True:
            user_input = input("Please enter 'coil number, value' (e.g '1,True'): ")
            inputs = [x.strip() for x in user_input.split(",")]
            if len(inputs) != 2:
                print("Invalid input. Please enter 'coil number, value' (e.g '1,True')")
                continue
            if not inputs[0].isdigit():
                print("Invalid input. Please enter a number.")
                continue
            else:
                coil = int(inputs[0])
            if inputs[1].lower() == "true":
                value = True
            elif inputs[1].lower() == "false":
                value = False
            else:
                print("Invalid input. Please enter 'coil number, value' (e.g '1,True')")
                continue
            try:
                client.write_coil(coil, value)
            except Exception as e:
                print(f"Failed to write to coil {user_input}: {e}")
                continue
            print(f"Wrote True to coil {user_input}")

    except KeyboardInterrupt:
        logger.info("Received keyboard interrupt. Shutting down...")


if __name__ == "__main__":
    main()
