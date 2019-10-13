from Common import *

def makeRequireErrorString(callerData, completeArgs, description):
    s = makeFileLocationString(callerData.filename, callerData.lineno) + "\n"
    s += makeArgsErrorString(completeArgs) + "\n"
    s += description.format(args = completeArgs)
    return s

def require(condition, description):
    callerData = getCallerData()
    def TEST(func):
        @wraps(func)
        def do(*args, **kwargs):
            completeArgs = makeCompleteArgumentDict(func, args, kwargs)
            completeArgs = dictToNamedTuple(completeArgs, "Args")

            if not condition(completeArgs):
                s = makeRequireErrorString(callerData, completeArgs, description)
                raise Exception(s)

            return func(*args, **kwargs)

        return do

    return TEST