from Common import *

def makeEnsureErrorString(callerData, completeArgs, result, description, preserved = None):
    s = "Ensure failed at " + makeFileLocationString(callerData.filename, callerData.lineno)
    s += '\n' + makeArgsErrorString(completeArgs)
    if preserved:
        s += '\n' + str(preserved)
    s += '\n' + "Result = " + str(result)
    try:
        s += "\n" + description.format(args = completeArgs, result = result, old = preserved)
    except Exception as e:
        s += "\n" + "Description formatting failed: " + str(e)
    return s

def ensure(condition, description):
    callerData = getCallerData()
    def TEST(func):
        @wraps(func)
        def do(*args, **kwargs):
            completeArgs = makeCompleteArgumentDict(func, args, kwargs)
            completeArgs = dictToNamedTuple(completeArgs, "Args")

            preserved = preserveValues(getattr(do, PRESERVER_ATTRIBUTE, []), completeArgs)

            result = func(*args, **kwargs)

            if condition.__code__.co_argcount == 3:
                preserved = dictToNamedTuple(preserved, "Old")
                if not condition(completeArgs, result, preserved):
                    raise Exception(makeEnsureErrorString(callerData, completeArgs, result, description, preserved))
            else:
                if not condition(completeArgs, result):
                    raise Exception(makeEnsureErrorString(callerData, completeArgs, result, description))

            return result
        return do

    return TEST