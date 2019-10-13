from Common import *

def getArgumentTypeMismatch(args, requirments):
    mismatches = {}
    for (k, v) in requirments.items():
        if k == 'RESULT':
            pass
        elif type(args[k]) != v:
            mismatches[k] = (args[k], v)
    return mismatches

def makeTypeMismatchString(mismatches: dict):
    s = 'Type mismatch' + '\n'
    for k, (v, t) in mismatches.items():
        s += f"Arg {k} = {v}, which is type {type(v)}, should have type {t}"
    return s

def types(**requirments):
    callerData = getCallerData()
    def TEST(func):
        @wraps(func)
        def do(*args, **kwargs):
            completeArgs = makeCompleteArgumentDict(func, args, kwargs)
            mismatches = getArgumentTypeMismatch(completeArgs, requirments)

            if mismatches:
                print(makeTypeMismatchString(mismatches))
                raise Exception

            result = func(*args, **kwargs)

            if 'RESULT' in requirments:
                if type(result) != requirments['RESULT']:
                    expected = requirments['RESULT']
                    print("Failed typecheck at", makeFileLocationString(callerData.filename, callerData.lineno))
                    completeArgs = dictToNamedTuple(completeArgs, 'Args')
                    print(completeArgs)
                    print(f"Result = {result}, type {type(result)}. Expected type {expected}")
                    raise Exception

            return result

        passPreservers(do, func)
        return do

    return TEST