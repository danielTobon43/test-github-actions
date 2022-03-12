from .context import script
from script import sum


def test_sum():
    assert sum(3, 2) == 5
    assert sum(-3, 3) == 0
    assert sum(-5, -5) == -10
