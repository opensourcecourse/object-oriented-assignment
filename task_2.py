"""A module which implements a gloriously inefficient 1D array class."""


class IncompatibleArrayOperationError(ValueError):
    """Raised when an operation is attempted on incompatible arrays."""


class InvalidEntryError(ValueError):
    """Raised when the input is not valid."""


class Array1D:
    """Class that behaves similar to numpy arrays, but for 1D data."""
