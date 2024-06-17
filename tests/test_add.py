import pytest
from typing import Union

from main import add


@pytest.mark.parametrize(
    "a, b, expected",
    [(1, 2, 3), (1.0, 2.0, 3.0), (1, 2.0, 3.0), (1.0, 2, 3.0), (0, 0, 0), (-1, -1, -2)],
)
def test_add(a: Union[int, float], b: Union[int, float], expected: Union[int, float]):
    result = add(a, b)

    assert result == expected
