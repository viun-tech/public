import pytest
from PIL import Image


@pytest.fixture()
def screw_image(shared_datadir) -> Image:
    yield Image.open(str(shared_datadir / "screw.png"))
