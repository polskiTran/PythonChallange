def approx_fixed_point(f, x, epsilon=1e-15):
    """Return True if f(x) is close to x.
    >>> approx_fixed_point(lambda x: x, 0.0)
    True
    >>> approx_fixed_point(lambda x: x, 3.0)
    True
    >>> approx_fixed_point(lambda x: cos(x) - x, 1.0)
    False
    """
    return abs(f(x) - x) < epsilon

# fixed pointed iteration to find Dottie's number
def fixed_point_iteration(f, x=1.0):
    """Find a fixed point of f(x) using fixed point iteration.
    >>> fixed_point_iteration(lambda x: cos(x), 1.0)
    (0.7390851332151611, 86)
    >>> fixed_point_iteration(lambda x: sin(x) + x, 3.0)
    (3.141592653589793, 3)
    """
    step = 0
    while not approx_fixed_point(f, x):
        x = f(x)
        step += 1
    return x, step

# Newton's method to find a zero of f(x)
def newton_find_zero(f, df, x=1.0, epsilon=1e-15, step=0):
    """Find a zero of f(x) using Newton's method.
    >>> newton_find_zero(lambda x: sin(x), lambda x: cos(x), 3.0)
    (3.141592653589793, 3)
    >>> newton_find_zero(lambda x: cos(x) - x, lambda x: -sin(x) - 1, 1.0)
    (0.7390851332151607, 4)
    """
    if abs(f(x)) < epsilon:
        return x, step
    else:
        return newton_find_zero(f, df, x - f(x) / df(x), epsilon, step + 1)




if __name__ == "__main__":
    from math import sin, cos
    import doctest
    doctest.testmod(verbose=True)
