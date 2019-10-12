def assertGreater(lhs, rhs):
    if lhs <= rhs:
        raise AssertionError(str(lhs) )