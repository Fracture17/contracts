from Common import *
from _Contract import Condition

def passPreservers(inner, func):
    setattr(inner, PRESERVER_ATTRIBUTE, getattr(func, PRESERVER_ATTRIBUTE, []))

def preserve(preserver):
    def TEST(func):
        @wraps(func)
        def inner(*args, **kwargs):
            return func(*args, **kwargs)

        if not hasattr(func, PRESERVER_ATTRIBUTE):
            setattr(func, PRESERVER_ATTRIBUTE, [])
        getattr(func, PRESERVER_ATTRIBUTE).append(preserver)

        passPreservers(inner, func)
        return inner
    return TEST

class preserve(Condition):
    def __init__(self, preserver):
        super().__init__(lambda : True)
        self.preserver = preserver

    def __call__(self, func):
        inner = super().__call__(func)
        if not hasattr(func, PRESERVER_ATTRIBUTE):
            setattr(func, PRESERVER_ATTRIBUTE, [])
        getattr(func, PRESERVER_ATTRIBUTE).append(self.preserver)
        passPreservers(inner, func)
        return inner