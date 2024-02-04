import pytest
from JuliaSet import calc_pure_python

@pytest.mark.parametrize("desired_width, max_iterations", [
    (1000, 300),
    (100, 300),
    (100, 100),
])

# Test the pure python implementation with varying width and max_iterations
def test_calc_pure_python_varying_width_max_iterations(desired_width, max_iterations):
    """Test the pure python implementation with varying width and max_iterations"""
    output = calc_pure_python(desired_width, max_iterations)
    assert isinstance(output, list)
    assert sum(output) >= 0
    assert sum(output) <= max_iterations * (desired_width ** 2)

    if desired_width == 1000 and max_iterations == 300:
        assert sum(output) == 33219980
    elif desired_width > 1000 and max_iterations > 300:
        assert sum(output) > 33219980
    elif desired_width < 1000 and max_iterations < 300:
        assert sum(output) < 33219980

# Test the pure python implementation without varying width and max_iterations
def test_calc_pure_python():
    """Test the pure python implementation"""
    desired_width = 1000
    max_iterations = 300
    output = calc_pure_python(desired_width, max_iterations)
    assert sum(output) == 33219980




