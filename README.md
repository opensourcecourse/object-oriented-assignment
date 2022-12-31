# Object-Oriented assignment

The goal of this assignment is not to make you an expert in OO design (easily a full semester course)
but to introduce you to some basic OO features of python.


# Task 1: Fun with classes (5 pts)

Look at `task_1.py` and fill in the implementations indicated by the comments.
You can run `pytest test_task_1.py` to see if your implementations are meeting
the specifications.

# Task 2: 1D array (20 points)

For task 2 we will create a 1D array object patterned after numpy's
[ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html), although we will completely
disregard efficiency. Start by looking at task_1.py and fill in the implementation to meet the
following requirements:


1. Implement the `__init__` to take a Sequence (tuple, lists, etc.) as the first input argument. 

2. Ensure each element is a basic numeric type (float, int, complex, None) else raise InvalidEntryError.

3. Implement the `__str__` and `__repr__` methods. If the len < 10 'Array1D[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]'
   showing each element. If it is greater than 10 `Array1D[...]`

4. Make sure the Array1D implements the Sequence protocol. Specifically, it should be iterable,
   indexible, membership checks should work, and slicing should return Array1D instances with a
   a subset of data.

5. Implement operators: add, subtract, true divide, floor divide, power. Each one should work
   with an array of equal size, an array of size 1, or a single number. This should work if
   the array or the number is first. (hint: `__add__` and `__radd__` are both needed). If the
   array's are not compatible, a IncompatibleArrayOperationError should be raised.

You can see how your implementation is performing by running `pytest test_task_1.py` after installing
pytest.




