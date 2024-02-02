#!/usr/bin/env python3
"""
Simulates a machine that opens a case, adds images to it, and requests inspection results.

Non-deterministic failures are introduced to simulate real-world conditions:

- The machine can fail to set a coil.
- The machine can set the wrong coil.
- The machine can reset all coils to 0/False.
- The machine can introduce latency.
- The machine can restart the workflow.
- The machine can disconnect and reconnect the modbus client.

Usage: modbus_test_loop.py [OPTIONS]

Options:
  -p, --port INTEGER  Modbus server port (default: 502)
  -h, --host TEXT     Modbus server host (default: localhost)
  -c, --chaos         Enable chaos (default: False)
  --help              Show this message and exit.

Dependencies:
    - pymodbus

Logging:
    Logs events of INFO and higher levels, and prints messages to the console.

Exit:
    The script can be interrupted using Ctrl+C or sending a KeyboardInterrupt.

Note:
    Ensure that a Modbus server is running on localhost and the specified port before using this client.
"""
import logging
import random
import sys
import time
from enum import Enum

import click
from avis_agent.core.commands import (
    AddImageCommand,
    GetCaseInspectionResultCommand,
    StartCaseCommand,
)
from avis_agent.core.responses import (
    CommandFailedResponse,
    CommandSuccessfulResponse,
    QualityTestFailedResponse,
    QualityTestSuccessfulResponse,
    QualityTestUncertainResponse,
)
from avis_agent.signal.impl.modbus_tcp import CommandCoilSettings, ResponseCoilSettings
from pymodbus.client import ModbusTcpClient


class ChaosProbability(Enum):
    LATENCY = 0.2  # 20% chance of introducing latency
    RESET_ALL_COILS = 0.1  # 10% chance of resetting all coils
    RESTART = 0.1  # 10% chance of restarting the workflow
    DISCONNECT = 0.1  # 10% chance of disconnecting the client


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class CoilManager:
    def __init__(self, client, chaos):
        self.client = client
        self.machine_coils = CommandCoilSettings()
        self.agent_coils = ResponseCoilSettings()
        self.coils = self.initialize_coils()
        self.chaos = chaos

    def initialize_coils(self):
        return {
            "agent_ready": self.agent_coils.ready_coil_idx,
            "agent_success": self.agent_coils.coil_mapping[CommandSuccessfulResponse],
            "agent_fail": self.agent_coils.coil_mapping[CommandFailedResponse],
            "agent_quality_success": self.agent_coils.coil_mapping[
                QualityTestSuccessfulResponse
            ],
            "agent_quality_fail": self.agent_coils.coil_mapping[
                QualityTestFailedResponse
            ],
            "agent_quality_uncertain": self.agent_coils.coil_mapping[
                QualityTestUncertainResponse
            ],
            "machine_ready": self.machine_coils.ready_coil_idx,
            "machine_startcase": self.machine_coils.coil_mapping[StartCaseCommand],
            "machine_addimage": self.machine_coils.coil_mapping[AddImageCommand],
            "machine_getresults": self.machine_coils.coil_mapping[
                GetCaseInspectionResultCommand
            ],
        }

    @property
    def all_coils(self):
        return list(self.coils.values())

    def set_coil(self, coil_key, value, chaos=True):
        coil = self.coils[coil_key]
        try:
            if chaos:
                coil = self.introduce_chaos(coil)
            self.client.write_coil(coil, value)
            logger.info(f"Set coil {coil_key} ({coil}) to {value}")
            return True
        except Exception as e:
            logger.error(f"Failed to write to coil {coil_key} ({coil}): {e}")
            self.client.close()
            self.client.connect()
            return False

    def wait_for_coil(self, coil_key, expected_value, timeout=30):
        """Wait for a specific coil to have a certain value."""
        end_time = time.time() + timeout
        while time.time() < end_time:
            if not self.read_coil(coil_key, expected_value):
                continue
            else:
                return True
        return False

    def read_coil(self, coil_key, expected_value):
        coil = self.coils[coil_key]
        try:
            result = self.client.read_coils(coil, 1)
            if result.bits[0] == expected_value:
                return True
        except Exception as e:
            logger.error(f"Failed to read coil {coil_key} ({coil}): {e}")
            self.client.close()
            self.client.connect()
        return False

    def wait_for_agent_ready(self):
        """Wait for only ready coil of agent to be set."""
        while True:
            other_coil_on = any(
                self.read_coil(coil_key, True)
                for coil_key in [
                    "agent_success",
                    "agent_fail",
                    "agent_quality_success",
                    "agent_quality_fail",
                    "agent_quality_uncertain",
                ]
            )
            if not other_coil_on and self.wait_for_coil("agent_ready", True):
                return True

    def introduce_chaos(self, coil):
        choice = random.random()
        sleep_time = random.randint(1, 10)

        if choice < ChaosProbability.LATENCY.value:
            logger.info(f"Introducing latency: Sleeping for {sleep_time}s")
            time.sleep(sleep_time)

        if choice < ChaosProbability.RESET_ALL_COILS.value:
            logger.warning("Chaos: Resetting all coils!")
            self.reset(reset_ready=True)
            logger.warning(
                f"Sleeping for {sleep_time}s before setting ready coil on again"
            )
            time.sleep(sleep_time)
            self.set_coil("machine_ready", True, chaos=False)

        return coil

    def reset(self, reset_ready=False):
        coils = [
            "machine_startcase",
            "machine_addimage",
            "machine_getresults",
        ]
        if reset_ready:
            coils.append("machine_ready")
        for coil_key in coils:
            logger.info(f"Resetting coil {coil_key} ({self.coils[coil_key]})")
            self.set_coil(coil_key, False, chaos=False)


@click.command()
@click.option("-p", "--port", default=502, help="Modbus server port (default: 502)")
@click.option(
    "-h", "--host", default="localhost", help="Modbus server host (default: localhost)"
)
@click.option(
    "-c", "--chaos", default=False, help="Enable chaos (default: False)", is_flag=True
)
def main(host: str, port: int, chaos: bool):
    client = ModbusTcpClient(host, port=port)
    coil_manager = CoilManager(client, chaos)
    coil_manager.reset(reset_ready=True)

    try:
        while True:
            ############  Machine Ready state ############
            ##############################################
            coil_manager.set_coil("machine_ready", True)
            if not coil_manager.wait_for_agent_ready():
                coil_manager.reset()
                continue

            #################  Open case #################
            ##############################################
            if coil_manager.set_coil(
                "machine_startcase", True
            ) and coil_manager.wait_for_coil("agent_success", True):
                coil_manager.set_coil("machine_startcase", False)

            elif coil_manager.wait_for_coil("agent_fail", True):
                coil_manager.set_coil("machine_startcase", False)
                coil_manager.set_coil("machine_ready", True)
                continue

            if not coil_manager.wait_for_agent_ready():
                coil_manager.reset()
                continue

            if chaos and (random.random() < ChaosProbability.RESTART.value):
                logger.warning("Chaos: Restarting the workflow!")
                continue

            ################  Add images #################
            ##############################################
            for _ in range(random.randint(1, 3)):
                time.sleep(random.randint(1, 3))
                coil_manager.set_coil("machine_addimage", True)
                if coil_manager.wait_for_coil("agent_success", True):
                    coil_manager.set_coil("machine_addimage", False)
                elif coil_manager.wait_for_coil("agent_fail", True):
                    coil_manager.set_coil("machine_addimage", False)
                    coil_manager.set_coil("machine_ready", True)
                    break
                if not coil_manager.wait_for_agent_ready():
                    coil_manager.reset()
                    continue

            if chaos and (random.random() < ChaosProbability.RESTART.value):
                logger.warning("Chaos: Restarting the workflow!")
                continue

            #######  Get case inspection results #########
            ##############################################
            coil_manager.set_coil("machine_getresults", True)
            if coil_manager.wait_for_coil("agent_quality_uncertain", True):
                coil_manager.set_coil("machine_getresults", False)
            elif coil_manager.wait_for_coil("agent_fail", True):
                coil_manager.set_coil("machine_getresults", False)
                coil_manager.set_coil("machine_ready", True)

            if chaos and (random.random() < ChaosProbability.DISCONNECT.value):
                logger.warning("Chaos: Disconnecting the client!")
                client.close()
                time.sleep(random.randint(2, 6))
                client = ModbusTcpClient(host, port=port)
                logger.warning("Chaos: Reconnected the client!")
    finally:
        coil_manager.reset(reset_ready=True)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Received keyboard interrupt. Shutting down...")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        sys.exit(1)
