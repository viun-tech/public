# AVIS Agent

This python package implements the AVIS Agent and its different integrations. For the full user documentation please
read the document: https://docs.google.com/document/d/1guod4Jlx5C179G7zVZfgsdofoqECzs7NGVWd-eoswI0/edit?usp=sharing.

The AVIS agent enables manufacturing machines to communicate with the AVIS backend to open inspection cases, upload
images, control a camera and get inspection results.

The AVIS Agent is a state machine simplifying the communication between a manufacturing machine, the AVIS Platform API,
and the camera. A single agent receives information and commands from a single manufacturing machine and controls a
single camera.

## Pre-requisites

* Python ^3.9,<3.12

## Installation

First create the log directory and assign the correct permissions (the agent expects this directory to exist):

```commandline
mdkir -p /var/log/avis_agent
chown -R pi:pi /var/log/avis_agent
```

`poetry install --with luxonis`.


### Install the systemd service

First make sure that the log directory exists and has the correct permissions (see [Installation](#installation)).

Replace `pi:pi` with the user and group that will run the agent.

Copy the file `systemd/avis_agent.service` in `/etc/systemd/system/avis_agent.service` on the server.

Then run the following commands:

```commandline
sudo systemctl daemon-reload
sudo systemctl enable avis_agent.service
sudo systemctl start avis_agent.service
```

The agent will now start automatically when the server starts and restart in case of failure.

To get the logs (stdout/stderr) of the agent, run the following command:

```commandline
sudo journalctl -u avis_agent.service -f
```

To get the status of the agent, run the following command:

```commandline
sudo systemctl status avis_agent.service
```

### Logging

A rotating file handler is configured to log the agent's activity. The log files are located in `/var/log/avis_agent/`.

5 files of 100 MB are kept. The log files are rotated once they are full.

The stdout and stderr of the process (managed by systemd) are also logged to `/var/log/avis_agent/stdout.log`
and `/var/log/avis_agent/stderr.log`.

You can read the logs in real time with the following command:

```commandline
tail -f /var/log/avis_agent/*
```

# Usage

Do not forget to generate the openapi backend client before running the agent (see [Installation](#installation))

```bash
poetry run avis_agent --config agent/.env
```

or if using the systemd service:

```bash
sudo systemctl start avis_agent.service
```

# Configuration

The agent uses [pydantic-settings](https://docs.pydantic.dev/latest/usage/pydantic_settings/) to manage its
configuration.

The configuration can be passed to the agent in 3 different ways:

* environment variables
* a configuration file (either env file or json file)
* a combination of both

The agent will look for the configuration in the following order:

1. environment variables
2. configuration file

This allows to use environment variables to override the configuration file.

You can create a new env file (an example is provided in `.env`) and pass it to the agent with the ̀̀`--config` option:

```commandline
poetryrun avis_agent --config .mylocal.env
```

You can override the configuration file with environment variables. The following will use all the config keys found in
the
file `.mylocal.env` and override the `AGENT_CAMERA` key with the environment variable `AGENT_CAMERA`:

```commandline
export AGENT_CAMERA='{"name": "oak_d_poe", "image_path": "image.png"}'
poetry run avis_agent --config .mylocal.env
```

Alternatively, the configuration can be specified in a json file. For example in `config.json`

```json
     {
  "camera": {
    "image_path": "image.png",
    "name": "oak_d_poe",
    "resolution": "1080p",
    "fixed_focus": 177
  },
  "backend": {
    "name": "avis",
    "api_key": "<redacted>",
    "team_id": 1,
    "inspection_object_id": 1,
    "uri": "https://avis.vu.engineering"
  },
  "signal": {
    "name": "modbus_tcp",
    "host": "localhost",
    "port": 502,
    "polling_interval": 0.1,
    "command_coil_settings": {
      "coil_mapping": {
        "ReadyCommand": 12,
        "StartCaseCommand": 13,
        "AddImageCommand": 14,
        "GetCaseInspectionResultCommand": 15
      }
    },
    "response_coil_settings": {
      "coil_mapping": {
        "ReadyResponse": 16,
        "CommandSuccessfulResponse": 17,
        "CommandFailedResponse": 18,
        "QualityTestFailedResponse": 19,
        "QualityTestUncertainResponse": 20
      }
    }
  }
}
```

Then run the agent with the following command:

```commandline
poetry run avis_agent --config config.json
```

## Configuration keys

### Failures and retries

Every integration (backend, signal, camera) has configuration keys that allow to configure how the agent will behave in
case of failure of an operation done by the integration. They are all optional and have default values. They are as
follows:

* `timeout`: the timeout in seconds before the agent gives up (float). The default value is 10s.
* `max_retries`: the maximum number of retries before the agent gives up (int). The default value is 3.
* `wait_fixed`: the time in seconds to wait between each retry (float). The default value is 1s.
* `wait_random`: added jitter to the wait time between each retry (float). This is a range ̀`Tuple[float, float]`, a
  random duration will be picked between the 2 values. The default value is `[0, 1.5]`.

### AGENT_CAMERA

#### [Luxonis OAK-D PoE](https://shop.luxonis.com/collections/oak-cameras-1/products/oak-d-s2-poe?variant=43146876551391)

```json
{
  "name": "oak_d_poe",
  "image_path": "image.png",
  "resolution": "1080p",
  "fixed_focus": 177,
  "crop": {
    "xmin": 0.2,
    "ymin": 0.2,
    "xmax": 0.8,
    "ymax": 0.8
  },
  "device_info": "169.254.1.222"
}
```

* `image_path` is the path to the file that the camera will use to save the image. The file will be overwritten every
  time a new image is taken.
* `resolution` (optional) is the resolution of the camera. It can be `1080p` or `4k`. If not specified, the camera will
  use `1080p`.
* `fixed_focus` (optional) is the distance in mm at which the camera is focused. If not specified, the camera will use
  autofocus mode.
* `crop` (optional) is the crop that will be applied to the image. The crop is defined by 4 values between 0 and 1
  representing the percentage of the image that will be kept (̀`xmin` and `ymin` are the coordinates of the top left
  corner and `xmax` and `ymax` are the coordinates of the bottom right corner. These coordinates are normalized for the
  size of the image and so the values should be between 0 and 1). If not specified, the image will not be
  cropped.
* `device_info` (optional) is the IP address (or MxID or USB port name) of the camera. If not specified, the agent will
  search for available devices that are connected either by USB port or are on the LAN (same subnet).
  See https://docs.luxonis.com/projects/hardware/en/latest/pages/guides/getting-started-with-poe/#how-it-works
  and https://docs.luxonis.com/projects/hardware/en/latest/pages/guides/getting-started-with-poe/#manually-specify-device-ip
  for more information.

#### Mock camera

A mock camera is available for testing purposes. It will generate a random image every time a new image is taken.

```json
{
  "name": "mock",
  "image_path": "image.png"
}
```

* `image_path` is the path to the file that the camera will use to save the image. The file will be overwritten every
  time a new image is taken.

### AGENT_BACKEND

```json
{
  "name": "avis",
  "api_key": "<redacted>",
  "team_id": 2,
  "inspection_object_id": 23,
  "uri": "https://avis.vu.engineering"
}
```

* `api_key` is a valid API key for the AVIS backend
* `team_id` is the ID of the team to use
* `inspection_object_id` is the ID of the inspection object to use
* `uri` is the URI of the AVIS backend

### AGENT_SIGNAL

#### Modbus TCP

Modbus TCP is a communication protocol that is used by many manufacturing machines. The agent can be configured to
communicate with a machine using this protocol.

```json
{
  "name": "modbus_tcp",
  "host": "localhost",
  "port": 502,
  "command_coil_settings": {
    "coil_mapping": {
      "ReadyCommand": 12,
      "StartCaseCommand": 13,
      "AddImageCommand": 14,
      "GetCaseInspectionResultCommand": 15
    }
  },
  "response_coil_settings": {
    "coil_mapping": {
      "ReadyResponse": 16,
      "CommandSuccessfulResponse": 17,
      "CommandFailedResponse": 18,
      "QualityTestSuccessfulResponse": 17,
      "QualityTestFailedResponse": 19,
      "QualityTestUncertainResponse": 19
    }
  }
}
```

* `host` is the IP address of the modbus server
* `port` is the port of the modbus server
* `command_coil_settings` (optional) is the configuration for the coils that will be used to send commands to the modbus
  server
    * `coil_mapping` is a mapping between the command name and the coil index (see explanations below)
* `response_coil_settings` (optional) is the configuration for the coils that will be used to receive responses from the
  modbus
  server
    * `coil_mapping` is a mapping between the response name and the coil index (see explanations below)

The `coil_mapping` is a mapping between the name of the command/response and the coil index.

The following commands are available to be mapped (see `avis_agent.core.commands`):

* `ReadyCommand`: the machine is ready to send commands
* `StartCaseCommand`: the agent should start a new case
* `AddImageCommand`: the agent should add an image to the current case
* `GetCaseInspectionResultCommand`: the agent should get the inspection result of the current case

The following responses are available to be mapped (see `avis_agent.core.responses`):

* `ReadyResponse`: the agent is ready to receive commands
* `CommandSuccessfulResponse`: the command was successful
* `CommandFailedResponse`: the command failed
* `QualityTestSuccessfulResponse`: the quality test passed successfully
* `QualityTestFailedResponse`: the quality test failed
* `QualityTestUncertainResponse`: the result of the quality test is uncertain

For more information about the modbus protocol, see
the [agent's usage manual](https://docs.google.com/document/d/1rL54tSs0Va9lE424Aj8N_thww1b4NjZ8UXeNYj2IWGE/)

Multiple commands or responses can be mapped to the same coil index. For example, the configuration above maps the
`CommandSuccessfulResponse` and the `QualityTestSuccessfulResponse` to the same coil index and the
`QualityTestFailedResponse` and the `QualityTestUncertainResponse` to the same coil index. Practically,
this means that the agent will send the same response to the machine if the command was successful or if the quality
test was successful. Similarly, the agent will send the same response to the machine if the quality test failed or if
the quality test result is uncertain.

By default the agent will use the following coil indices:

`command_coil_settings`:

* ReadyCommand: 0
* StartCaseCommand: 1
* AddImageCommand: 2
* GetCaseInspectionResultCommand: 3

`response_coil_settings`:

* ReadyResponse: 4
* CommandSuccessfulResponse: 5
* CommandFailedResponse: 6
* QualityTestSuccessfulResponse: 7
* QualityTestFailedResponse: 8
* QualityTestUncertainResponse: 9

**Please note that `command_coil_settings` and `response_coil_settings` are "all-or-nothing" configurations: either you
need to configure all the commands/responses you want to use in the mapping or you omit these keys and the defaults will
be used.**

#### CLI

The CLI integration is used for testing purposes. It allows to send commands to the agent from the command line.

```json
{
  "name": "cli"
}
```

## Instrumentation/telemetry

The agent uses [OpenTelemetry](https://opentelemetry.io/) to instrument its code and send telemetry to an observability
backend of your choice.

There are 2 configuration keys that allow to configure the telemetry. **Either both of them need to be specified or none
of them**:

* `instrumentation.traces_exporter_endpoint`: the endpoint to send the trace telemetry to. For
  example: `http://localhost:4317`. Can be a collector or a backend. The corresponding environment variable
  is `AGENT__INSTRUMENTATION_TRACES_EXPORTER_ENDPOINT`
* `instrumentation.metrics_exporter_endpoint`: the endpoint to send the meter telemetry to. For
  example: `http://localhost:4317`. Can be a collector or a backend. The corresponding environment variable
  is `AGENT__INSTRUMENTATION_METRICS_EXPORTER_ENDPOINT`

Corresponds to the following json:

```json
{
  "instrumentation": {
    "traces_exporter_endpoint": "http://localhost:4317",
    "metrics_exporter_endpoint": "http://localhost:4317"
  }
}
```

The execution of following is traced:

* any request made to the AVIS backend
* the capture of an image by the camera
* any response sent to the manufacturing machine
* any command received from the manufacturing machine

The duration of all of these operations is recorded and sent to the observability backend as histogram metrics.

Additionally, a heartbeat metric can be sent to the observability backend. The interval at which the heartbeat is sent
is controlled by the `heartbeat_interval` configuration key (int, in seconds):

```json
{
  "instrumentation": {
    "traces_exporter_endpoint": "http://localhost:4317",
    "metrics_exporter_endpoint": "http://localhost:4317",
    "heartbeat_interval": 60
  }
}
```

Or the corresponding environment variable `AGENT__INSTRUMENTATION_HEARTBEAT_INTERVAL`.

# Run the tests

### **!!! Please note that running the tests is not currently possible since they depend on the AVIS backend which is proprietary, closed-source code. This will be
fixed in the future !!!**

Install the dev dependencies

`poetry install --with dev,luxonis`.

Run the tests

```commandline
poetry run pytest
```

## Repository structure

The code is split in 4 differents directory:

1. `core`: this directory contains the agent state machine and the code required for the agent to function properly.
2. `backend`: this directory contains the necessary code to interact with the AVIS backend and the implementations of
   the processes when communicating with the AVIS backend.
3. `camera`: this directory contains the necessary code to interact with the camera connected to the agent. Any camera
   controller needs to extend the `AbstractCamera` class.
4. `signal`: this directory contains the necessary code to communicate with the manufacturing machine. Any communication
   protocol need to extend the `AbstractSignal` class.

In addition, to those 4 different directories, there is a `utils` directory for helpful scripts.

The main code to run the agent with its different integration is the in the file `__main__.py`

# Scripts

A few additional scripts are available in the `scripts` directory.

* `python/modbus_server.py`: start a modbus server locally
* `python/modbus_client.py`: start a modbus client locally that allows to send commands to the modbus server from the
  command
  line
* `python/modbus_test_loop.py`: simulates a machine that opens a case, adds images to it, and requests inspection
  results. It has built-in errors (failure to write coils, restarts, delays, etc...) to test the agent's robustness.
* `python/calibrate_camera.py`: can be used to find the right parameters to calibrate the camera.
* `bash/chaos.sh`: can be used to simulate a chaotic environment. It will randomly stop and start the agent and the
  modbus server and block network traffic to the AVIS backend for a random amount of time. Please note that this script
  requires both the agent and a local modbus server to be started with systemd (see `systemd` directory
  and `Installation` section)
