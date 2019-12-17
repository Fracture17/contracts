from tests.TestCode import *
from src.Contract import *
from hypothesis import given
from hypothesis.strategies import booleans
from pytest import raises
from src.ContractLevel import OFF


def test_debugLevel():
    assert QQQ(10,5) == 20

    assert T(2, 5, 2) == 10
    t = TTT(0)

    empty(29)


def test_code():
    assert QQQ(10,5) == 20

    assert T(2, 5, 2) == 10
    t = TTT(0)
    #t.x = 2
    with raises(PostConditionError):
        t.hey()


@given(booleans())
def test_require(b):
    c = require(lambda args: args.x == True)
    v = c(lambda x: x)
    if b == False:
        with raises(PreConditionError):
            v(b)
    else:
        v(b)

@given(booleans())
def test_ensure(b):
    c = ensure(lambda args, result: result == True)
    v = c(lambda x: x)
    if b == False:
        with raises(PostConditionError):
            v(b)
    else:
        v(b)

@given(booleans())
def test_invariant(b):
    class InvariantTest:
        def __init__(self, x):
            self.x = x

        def set(self, x):
            self.x = x

    c = invariant(lambda self: self.x == True)
    v = c(InvariantTest)
    if b == False:
        with raises(PostConditionError):
            O = v(b)
        O = v(True)
        O.x = False
        with raises(PreConditionError):
            O.set(b)
        O.x = True
        with raises(PostConditionError):
            O.set(b)
    else:
        O = v(b)
        O.set(b)
        O.x = False
        with raises(PreConditionError):
            O.set(b)


@types(x = int)
def v(x):
    pass

def test_types():
    with raises(PreConditionError):
        v("")
    v(2)