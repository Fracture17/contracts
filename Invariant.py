from Common import *

#Taken from dpcontracts
def shouldDoInvariant(name, func, cls):
    exceptions = ("__getitem__", "__setitem__", "__lt__", "__le__", "__eq__",
                  "__ne__", "__gt__", "__ge__", "__init__")

    if name.startswith("__") and name.endswith("__") and name not in exceptions:
        return False

    if not ismethod(func) and not isfunction(func):
        return False

    if getattr(func, "__self__", None) is cls:
        return False

    return True

def getMethodActualFirstLine(sourceLines):
    line = sourceLines[1]
    sourceLines = sourceLines[0]
    while not sourceLines[0].strip().startswith('def'):
        sourceLines = sourceLines[1:]
        line += 1
    return line

def invariantCheck(condition, description, callerFrame):
    def TEST(func):
        @wraps(func)
        def do(*args, **kwargs):
            completeArgs = makeCompleteArgumentDict(func, args, kwargs)
            completeArgs = dictToNamedTuple(completeArgs, "Args")

            #preserve

            if func.__name__ != '__init__':
                if not condition(completeArgs[0]):
                    x = getsourcelines(func)
                    L = getMethodActualFirstLine(x)
                    print("Precheck invariant at", makeFileLocationString(callerFrame.filename, callerFrame.lineno))
                    print("failed for method at", makeFileLocationString(callerFrame.filename, L))
                    print(completeArgs)
                    print(description)
                    raise Exception

            result = func(*args, **kwargs)

            if not condition(completeArgs[0]):
                x = getsourcelines(func)
                L = getMethodActualFirstLine(x)
                print("Postcheck invariant at", makeFileLocationString(callerFrame.filename, callerFrame.lineno))
                print("failed for method at", makeFileLocationString(callerFrame.filename, L))
                print(completeArgs)
                print(description)
                raise Exception

            return result
        return do

    return TEST


def invariant(condition, description):
    callerFrame = getCallerData()
    def TEST(cls):
        class InvariantContractor(cls):
            pass

        for name, value in [(name, getattr(cls, name)) for name in dir(cls)]:
            if shouldDoInvariant(name, value, cls):
                setattr(InvariantContractor, name,
                        invariantCheck(condition, description, callerFrame)(value))

        return InvariantContractor

    return TEST