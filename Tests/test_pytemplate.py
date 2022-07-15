# First-party/Local
import src.core
from src import __version__


def test_version():
    assert __version__ == "0.2.1"


def test_core():
    # Pass
    assert src.core.main() is None
