#!/usr/bin/env python3
import readline
import reader as rdr
import printer as pr
import mtypes as tp

# Repl environment
REPL_ENV = {'+': lambda a: mal_sum(a),
            '-': lambda a: mal_diff(a),
            '*': lambda a: mal_prod(a),
            '/': lambda a: mal_div(a)}


def mal_sum(x):
    a = 0
    for i in x:
        a += i
    return a


def mal_diff(x):
    if x:
        if len(x) > 1:
            a = x.pop(0)
            return a - mal_sum(x)
        else:
            return -x[0]
    else:
        print("Not enough arguments for - function, exiting")
        exit()


def mal_prod(x):
    a = 1
    for i in x:
        a *= i
    return a


def mal_div(x):
    if x:
        if len(x) > 1:
            a = x.pop(0)
            return a / mal_prod(x)
        else:
            return 1/x[0]
    else:
        print("Not enough arguments for / function, exiting")
        exit()


def atom_as_mal_type(atom):
    if isinstance(atom, str):
        return tp.MalSymbol(atom)
    else:
        return tp.MalNumber(atom)


def eval_ast(ast, repl_env):
    match ast.typ():
        # symbol
        case 3:
            val = ast.value()
            if val in repl_env.keys():
                return repl_env[ast.value()]
            else:
                print("Undefined symbol", val)
                exit()
        # list
        case 1:
            return list(map(lambda x: EVAL(x, repl_env), ast.value()))
        # everything else
        case _:
            return ast.value()


def READ(input):
    return rdr.read_str(input)


def EVAL(ast, repl_env):
    if ast.typ() == 1:
        if ast.nempty():
            val_ast = eval_ast(ast, repl_env)
            fn = val_ast.pop(0)
            return fn(val_ast)
        else:
            return ast
    else:
        return eval_ast(ast, repl_env)


def PRINT(input):
    # return pr.pr_str(input)
    return str(input)


def rep(input):
    return PRINT(EVAL(READ(input), REPL_ENV))


def main():
    while(True):
        try:
            line = input("user> ")
            print(rep(line))
        except EOFError:
            exit()


if __name__ == "__main__":
    main()
