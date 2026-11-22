import pytest

from calc import calculate


@pytest.mark.parametrize(
    ("a", "b", "operation", "expected"),
    [
        (4, 2, "+", 6),
        (4, 2, "-", 2),
        (4, 2, "*", 8),
        (4, 2, "/", 2),
    ],
)
def test_calculate(a, b, operation, expected):
    assert calculate(a, b, operation) == expected


def test_calculate_division_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculate(4, 0, "/")


def test_calculate_unknown_operation():
    with pytest.raises(ValueError, match="Unknown operation"):
        calculate(4, 2, "%")
