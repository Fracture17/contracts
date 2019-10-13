from functools import wraps
from inspect import signature
from collections import namedtuple
from inspect import isfunction, ismethod, iscoroutinefunction, getfullargspec, getsource, getsourcefile, getfile, stack, getsourcelines

PRESERVER_ATTRIBUTE = '__contract_preserved_values__'

def dictToNamedTuple(d: dict, name: str):
    return namedtuple(name, d.keys())(**d)

def makeCompleteArgumentDict(func, args, kwargs):
    s = signature(func)
    p = s.parameters
    build = {}
    for a, b in zip(args, p.keys()):
        build[b] = a
    for k, v in p.items():
        if v.default:
            if k not in build:
                build[k] = v.default
    for k, v in kwargs.items():
        build[k] = v

    return build

def makeArgsErrorString(args):
    return str(args)

def makeResultErrorString(result):
    return f"Result = {result}"

def makeDescriptionErrorString(description, args, result = ""):
    return description.format(args = args, result = result)

def makeTypesErrorString(args, requirements, mismatches):
    temp = str(args)
    temp += "\n" + str(requirements)
    temp += "\n" + str(mismatches)
    return temp

def makePreservedValuesErrorString(preserved):
    return str(preserved)

def makeFileLocationString(filename: str, lineNum):
    return f'File "{filename}", line {lineNum}'

def makeStringErrorThing(data, build, description):
    s = makeFileLocationString(data.filename, data.lineno)
    s += '\n' + makeArgsErrorString(build)
    s += "\n" + makeDescriptionErrorString(description, build)
    return s

def getCallerData():
    #third element because it gets the caller's caller's info
    return stack()[2]




def preserveValues(preservers, Args):
    preserved = {}
    for preserver in preservers:
        preserved.update(preserver(Args))
    return preserved










