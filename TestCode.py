from Contracts import require, ensure, types, invariant, preserve

def cond(args):
    return args.x == 2

@preserve(lambda args: {'z': args.z})
@types(RESULT = float, y = int, q = int)
@require(cond, "x = {args.x}, must = 3")
@require(lambda args: args.x == 2, "x = {args.x}, must = 3")
@ensure(lambda args, result, old: old.z == 2, "result should be 5")
@preserve(lambda args: {'y': args.y})
@ensure(lambda args, result: result == 10, "result hhhhhhh be {old.x}")
@require(cond, "x = {args.x}, must = 3")
def T(z, y, x = 18, q = 3):
    return z * y


@invariant(lambda self: self.x == 0, "invariant")
class TTT:
    @require(lambda x: True,0)
    def __init__(self, x):
        self.x = x

    @require(lambda x: True, 0)
    def hey(self):
        self.x = 10
        pass

if __name__ == 'main':
    print(T(2, 5, 2))
    x = TTT(0)
    x.hey()


