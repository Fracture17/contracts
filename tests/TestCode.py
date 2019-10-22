#from  import require, ensure, types, invariant, preserve
from src.Ensure import ensure
from src import require, ensure, types, invariant, preserve

def cond(args):
    return True
    return args.x == 10

@require(cond, "cool")
@require(lambda args: args.y == 5, 'ehehehe {args.x}')
@ensure(lambda args, result: result == 20)
@preserve(lambda args: {'x': args.x, 'y': args.y})
def QQQ(x, y = 10):
    return x * 2

@preserve(lambda args: {'z': args.z})
@types(RESULT = float, y = int, q = int)
@require(cond, "x = {args.x}, must = 3")
@require(lambda args: args.x == 2, "x = {args.x}, must = 3")
@ensure(lambda args, result, old: True, "result should be 5")
@preserve(lambda args: {'y': args.y})
#@ensure(lambda args, result: result == 10, "result hhhhhhh be {old.x}")
#@require(cond, "x = {args.x}, must = 3")
def T(z, y, x = 18, q = 3):
    return float(z * y)


@invariant(lambda self: self.x == 0)
class TTT:
    @require(lambda x: True,0)
    def __init__(self, x):
        self.x = x

    @preserve(lambda args: {'x': args.self.x})
    @require(lambda x: True, 0)
    @preserve(lambda args: {'x': args.self.x})
    @ensure(lambda args, result: True)
    def hey(self):
        self.x = 10
        pass

if __name__ == 'main':
    print(T(2, 5, 2))
    x = TTT(0)
    x.hey()


