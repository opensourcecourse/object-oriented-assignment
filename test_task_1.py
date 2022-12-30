"""
Tests for task_1's Array1D.

You need to first install pytest, then run this from the command line
via: `pytest test_task_1.py`
"""
import pytest

from task_1 import Array1D

INPUT_ARRAYS = (
    (1, 0, 0, 1),
    (1j+2, 0, 12),
    (0.0, 0.00001, 0.0),
    (None, 10, -10.0),
    tuple(range(1000)),
)


class TestInit:
    """Tests for initializing the Array1D with various parameters."""

    def test_empty(self):
        """Should be able to init empty array."""
        ar = Array1D()
        assert isinstance(ar, Array1D)

    @pytest.mark.parametrize("array_input", INPUT_ARRAYS)
    def test_list(self, array_input):
        """All INPUT_ARRAY entries should be valid."""
        ar = Array1D(array_input)
        assert isinstance(ar, Array1D)


