import django  # noqa

django.setup()  # noqa

import pytest  # noqa

# import all fixtures from avis so that we can use them in the agent's tests
from avis.tests.conftest import *  # noqa
from PIL import Image  # noqa


@pytest.fixture()
def screw_image(shared_datadir) -> Image:
    yield Image.open(str(shared_datadir / "screw.png"))
