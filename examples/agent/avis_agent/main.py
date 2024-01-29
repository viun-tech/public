import json
import logging
import os
from logging.handlers import RotatingFileHandler

import click
from avis_agent.backend.base import AbstractBackend
from avis_agent.camera.base import AbstractCamera
from avis_agent.core.base import Agent, AgentSettings
from avis_agent.signal.base import AbstractSignal

# Rotating log file
# 5 files of 100MB each are kept

# check if log directory exists and if the user has write permissions
# if not, log to the current directory
log_dir = "/var/log/avis_agent"
if not os.path.isdir(log_dir) or not os.access(log_dir, os.W_OK):
    log_dir = os.getcwd()

log_file = os.path.join(log_dir, "avis_agent.log")
log_format = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
formatter = logging.Formatter(log_format)
file_handler = RotatingFileHandler(
    log_file, maxBytes=100 * 1024 * 1024, backupCount=5
)  # 100MB per file, 5 backup files
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
logging.basicConfig(level=logging.INFO, handlers=[file_handler, stream_handler])
logger = logging.getLogger(__name__)


@click.command()
@click.option("-c", "--config", type=click.Path(exists=True), required=True)
def main(config: str):
    with open(config, "r") as f:
        try:
            raw_config = json.load(f)
            settings = AgentSettings(_env_file=None, **raw_config)
        except json.JSONDecodeError:
            settings = AgentSettings(_env_file=config)

    msg = f"Starting agent with config: {settings}"
    click.echo(msg)

    backend = AbstractBackend.build(settings.backend)
    camera = AbstractCamera.build(settings.camera)
    signal = AbstractSignal.build(settings.signal)
    agent = Agent(backend=backend, camera=camera, signal=signal, config=settings)

    agent.run()


if __name__ == "__main__":
    main()
