from Common import *

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