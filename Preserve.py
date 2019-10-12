from Common import *

#A preseve only works if there is an ensure below it
#A single ensure below it will make it work for ALL ensures, even the ones above it
def preserve(preserver):
    def TEST(func):
        @wraps(func)
        def inner(*args, **kwargs):
            return func(*args, **kwargs)

        if not hasattr(func, PRESERVER_ATTRIBUTE):
            setattr(func, PRESERVER_ATTRIBUTE, [])
        getattr(func, PRESERVER_ATTRIBUTE).append(preserver)

        return inner
    return TEST