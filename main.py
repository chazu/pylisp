import math

#code = "(sum 1 2)"
#expect = ["list", ["symbol", "sum"], ["int", 1], ["int", 2]]

def plus(args):
    return sum(args)

tests = [
    {"in": ["int", 27], "out": 27},
    {"in": ["symbol", "pi"], "out": math.pi },
    {"in": ["symbol", "+"], "out": plus },
    {"in": ["list", ["symbol", "+"], ["int", 10], ["int", 3]],
     "out": 13 }
]

immediate_types = [
    "int"
]

env = {
    "pi": math.pi,
    "+": plus
}

def _apply(operator, args):
    print(f"Applying {operator} to {args}")
    return operator(args)

def evaluate(ast, env):
    if ast[0] in immediate_types:
        return ast[1]
    elif ast[0] == "symbol":
        return env[ast[1]]
    elif ast[0] == "list":
        evaluated_ast = [evaluate(x, env) for x in ast[1:]]
        operator = evaluated_ast[0]
        args = evaluated_ast[1:]
        return _apply(operator, args)
    else:
        raise Exception("NOBODY TOLD ME HOW TO DO THAT")


if __name__ == "__main__":

    for test in tests:
        expect = test["out"]
        result = evaluate(test["in"], env)
        print(result)
        assert expect == result
