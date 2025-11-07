import pytest
from app.operations import add, subtract, multiply, divide

# Parametrized test data for addition
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),           # add_two_positive_integers
    (-2, -3, -5),        # add_two_negative_integers
    (2.5, 3.0, 5.5),     # add_two_positive_floats
    (-2.5, 3.0, 0.5),    # add_negative_and_positive_float
    (0, 0, 0),           # add_zeros
], ids=[
    "add_two_positive_integers",
    "add_two_negative_integers",
    "add_two_positive_floats",
    "add_negative_and_positive_float",
    "add_zeros"
])
def test_add(a, b, expected):
    """Test the add function with various inputs."""
    assert add(a, b) == expected

# Parametrized test data for subtraction
@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),           # subtract_two_positive_integers
    (-2, -3, 1),         # subtract_two_negative_integers
    (5.5, 2.0, 3.5),     # subtract_two_positive_floats
    (-2.5, -3.0, 0.5),   # subtract_two_negative_floats
    (0, 0, 0),           # subtract_zeros
], ids=[
    "subtract_two_positive_integers",
    "subtract_two_negative_integers",
    "subtract_two_positive_floats",
    "subtract_two_negative_floats",
    "subtract_zeros"
])
def test_subtract(a, b, expected):
    """Test the subtract function with various inputs."""
    assert subtract(a, b) == expected

# Parametrized test data for multiplication
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),           # multiply_two_positive_integers
    (-2, 3, -6),         # multiply_negative_and_positive_integer
    (2.5, 4.0, 10.0),    # multiply_two_positive_floats
    (-2.5, 4.0, -10.0),  # multiply_negative_float_and_positive_float
    (0, 5, 0),           # multiply_zero_and_positive_integer
], ids=[
    "multiply_two_positive_integers",
    "multiply_negative_and_positive_integer",
    "multiply_two_positive_floats",
    "multiply_negative_float_and_positive_float",
    "multiply_zero_and_positive_integer"
])
def test_multiply(a, b, expected):
    """Test the multiply function with various inputs."""
    assert multiply(a, b) == expected

# Parametrized test data for division
@pytest.mark.parametrize("a, b, expected", [
    (6, 3, 2.0),         # divide_two_positive_integers
    (-6, 3, -2.0),       # divide_negative_integer_by_positive_integer
    (5.5, 2.0, 2.75),    # divide_two_positive_floats
    (-5.5, 2.0, -2.75),  # divide_negative_float_by_positive_float
    (0, 5, 0.0),         # divide_zero_by_positive_integer
], ids=[
    "divide_two_positive_integers",
    "divide_negative_integer_by_positive_integer",
    "divide_two_positive_floats",
    "divide_negative_float_by_positive_float",
    "divide_zero_by_positive_integer"
])
def test_divide(a, b, expected):
    """Test the divide function with various inputs."""
    assert divide(a, b) == expected

def test_divide_by_zero():
    """Test that dividing by zero raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide(5, 0)