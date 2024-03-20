# Use the AVIS python client

**Please note that this example is provided as-is with no guarantees of support.**

This example shows how to interact with the AVIS API using the python client.

## Requirements
* python 3.10 or higher
* [poetry](https://python-poetry.org/)

## Installation
```bash
poetry install
```

## Run
```bash
poetry run python use_avis_client/main.py
```

## Usage in your project

In your `pyproject.toml` file, add the following dependency:

```toml
[tool.poetry.dependencies]
python = "^3.10"
use-avis-client = {path = "../use-avis-client", develop = true}
```

Then, in your code, you can use the `use_avis_client` package:

```python
from use_avis_client.main import (
    create_inspection,
    close_inspection,
    add_image_to_inspection,
    get_image_attributes,
)
from avis_client import Configuration

TEAM_ID = 1
CONFIGURATION_ID = 1
MEMBERSHIP_ID = 1
API_KEY = "1234"
API_URI = "https://avis.vu.engineering"
API_CONFIG = Configuration(host=API_URI, api_key={"ApiKeyAuth": API_KEY})
IMAGE_PATH = "image.png"

inspection_id = create_inspection(TEAM_ID, CONFIGURATION_ID, API_CONFIG)
image_id = add_image_to_inspection(TEAM_ID, inspection_id, IMAGE_PATH, API_CONFIG)
image_attributes = get_image_attributes(TEAM_ID, inspection_id, image_id, API_CONFIG)
close_inspection(inspection_id, MEMBERSHIP_ID, API_CONFIG)
```
