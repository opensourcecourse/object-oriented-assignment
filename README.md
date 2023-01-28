# Object-Oriented assignment

Object-oriented programming and design is an extensive topic (most universities offer a full
semester course). The goal of this assignment is not to make you an expert but to introduce
you to some basic OO features of python.

Once you have completed both tasks, create a new branch, push to origin, and open
a pull request. You can check the status of the GH actions (a separate window will
be inserted in the PR screen) to see how your implementation is doing. Remember what
you learned from the style assignment, readability still counts.

When you are finished with *both* tasks, create a new PR and ping the instructors 
(@opensourcecourse/instructors).

You will need to install pytest to complete this assignment. To do so, simply use `pip install pytest` or
`conda install pytest`.

Just like before, you can also run the style checking with pre-commit: `pre-commit run --all`.

# Task 1: Fun with classes (5 pts)

Look at `task_1.py` and fill in the implementations indicated by the comments.
Next, run `pytest test_task_1.py` to see if your implementations are meeting
the specifications. Fix the issues until all the tests pass.

# Task 2: 1D array (20 points)

For task 2 we will create a 1D array object patterned after numpy's
[ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html), although we will completely
disregard efficiency. Start by looking at task_1.py and fill in the implementation to meet the
following requirements:

1. Implement the `__init__` to *optionally* take a Sequence (tuple, lists, etc.) as the first input argument.
   If no input is provided use an empty list.

2. Ensure each element is a basic numeric type (float, int, complex, None) else raise `InvalidEntryError`.

3. Implement the `__str__` and `__repr__` methods, which should be the same. If the len < 10, and the inputs is
   `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` the output should be 'Array1D[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]'
   showing each element. If the input is greater than 10 it should be: `Array1D[...]`.

4. Make sure the Array1D implements the Sequence protocol. Specifically, it should be iterable,
   indexible, membership checks should work, and slicing should return Array1D instances with
   a subset of the data.

5. Implement operators: add, subtract, true divide, floor divide, power. Each one should work
   with an array of equal size, an array of size 1 (for broadcasting), or a single number. This should work if
   the array or the number is first in the operation. E.g., `array + 1` should be identical to `1 + array`.
   (hint: `__add__` and `__radd__` are both needed). If the arrays are not compatible, 
   an `IncompatibleArrayOperationError` should be raised.

You can see how your implementation is performing by running `pytest test_task_2.py`.
