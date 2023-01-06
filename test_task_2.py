"""
Tests for task_1's Array1D.

You need to first install pytest, then run this from the command line
via: `pytest test_task_1.py`
"""
import sys
from operator import add, floordiv, mul, pow, sub, truediv

import pandas as pd
import pytest

from task_2 import Array1D, IncompatibleArrayOperationError, InvalidEntryError

INPUT_ARRAYS = (
    (1, 0, 0, 1),
    (1j + 2, 0, 12),
    (0.0, 0.00001, 0.0),
    (None, 10, -10.0),
    range(100),
    [1, 2, 3],
)


@pytest.fixture(params=INPUT_ARRAYS)
def array_input(request):
    """Parameterized fixture which is input to the array."""
    return request.param


def test_numpy_not_in_loaded_modules(self):
    """Numpy should not be in the imported modules."""
    assert "numpy" not in sys.modules


class TestInit:
    """Tests for initializing the Array1D with various parameters."""

    def test_empty(self):
        """Should be able to init empty array."""
        ar = Array1D()
        assert isinstance(ar, Array1D)

    def test_list(self, array_input):
        """All INPUT_ARRAY entries should be valid."""
        ar = Array1D(array_input)
        assert isinstance(ar, Array1D)

    def test_nested_list_raises(self):
        """A nested list should raise, only supports 1D."""
        bad_input = [1, 2, [2, 3]]
        with pytest.raises(InvalidEntryError):
            Array1D(bad_input)


class TestSequence:
    """Tests for the 'sequenceyness' of Arrray1D."""

    def test_to_list(self, array_input):
        """The conversion to and from a list should be lossless."""
        array = Array1D(array_input)
        assert list(array) == list(array_input)

    def test_len(self, array_input):
        """Array1D should have a len == to input len."""
        assert len(Array1D(array_input)) == len(array_input)

    def test_iterate(self, array_input):
        """Array 1D should be iterable."""
        array = Array1D(array_input)
        for el1, el2 in zip(array, array_input):
            assert el1 == el2

    def test_membership_check(self, array_input):
        """Ensure *in* works elementwise."""
        array = Array1D(array_input)
        for el in array_input:
            assert el in array

    def test_slice(self):
        """Ensure a slice from the array returns a sub array."""
        array_inp = INPUT_ARRAYS[0]
        array = Array1D(array_inp)
        array_slice = array[1:-2]
        assert isinstance(array_slice, Array1D)
        assert list(array_slice) == array_inp[1:-2]


class TestRepresentation:
    """Ensure str and repr are set."""

    def test_str_gt_10(self):
        """Ensure array str is truncated for long ones."""
        ar = Array1D(range(11))
        assert str(ar) == "Array1D[...]"

    def test_str_le_10(self):
        """Ensure all elements printed for short strs."""
        ar = Array1D(range(10))
        expected = f"Array1D{str(list(range(10)))}"
        assert str(ar) == expected


class TestArithmetic:
    """Tests for arithmetic operations on Array1D."""

    operators = (add, floordiv, truediv, sub, mul, pow)

    def test_self_operations(self, array_input):
        """Test array operating on itself."""
        array = Array1D(array_input)
        # test each of the operators
        for op in self.operators:
            result = op(array, array)
            for el1, el2 in zip(result, array):
                assert el1 == op(el2, el2)

    def test_uneven_array_raises(self, array_input):
        """Arrays of different lengths should not be compatible."""
        array1 = Array1D(array_input)
        array2 = Array1D(array_input[:-1])

        if len(array2) == 1:  # len 1 *should* work with other lens
            return

        for op in self.operators:
            with pytest.raises(IncompatibleArrayOperationError):
                op(array1, array2)

    def test_one_null_broadcast(self, array_input):
        """Ensure an operation with one null results in all null."""
        array = Array1D(array_input)
        null_array = Array1D([None])
        for op in self.operators:
            result1 = op(array, null_array)
            assert all([pd.isnull(x) for x in result1])
            result2 = op(null_array, array)
            assert all([pd.isnull(x) for x in result2])
