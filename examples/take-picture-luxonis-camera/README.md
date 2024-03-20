# Take pictures with a Luxonis camera

**Please note that this example is provided as-is with no guarantees of support.**

This example shows how to take pictures with a Luxonis camera (OAK-D) and save them to disk.

## Requirements

* python 3.10 or higher
* [poetry](https://python-poetry.org/)
* A luxonis camera (OAK-D)

## Installation

```bash
poetry install
```

## Run

```bash
poetry run python take_picture_luxonis_camera/main.py
```

## Usage in your project

In your `pyproject.toml` file, add the following dependency:

```toml
[tool.poetry.dependencies]
python = "^3.10"
take-picture-luxonis-camera = {path = "../take-picture-luxonis-camera", develop = true}
```

Then, in your code, you can use the `take_picture_luxonis_camera` package:

```python
from take_picture_luxonis_camera.main import (
    OakDPOECamera,
    CameraSettings,
    CameraResolution,
    CropCoordinates,
)

config = CameraSettings(
        device_info="192.168.1.80",
        resolution=CameraResolution.the_1080_p,
        fixed_focus=177,
        # crop rectangle with width 550 and height 400
        # that is located 819px from the left edge of the image and 240px from the top edge
        crop=CropCoordinates(left=819, upper=240, right=1369, lower=640),
    )
camera = OakDPOECamera(config)
camera.start()
image = camera.capture_image()
image.show()
camera.stop()
```
