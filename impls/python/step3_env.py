#!/usr/bin/env python3
import readline
import reader as rdr
import printer as pr
import mtypes as tp
import env

# Repl environment
Base_functions = {'+': lambda a: mal_sum(a),
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
    elif isinstance(atom, tp.Mal):
        return atom
    else:
        return tp.MalNumber(atom)


def eval_ast(ast, repl_env):
    match ast.typ():
        # symbol
        case 3:
            val = ast.value()
            if repl_env.find(val):
                return repl_env.get(val)
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
            felem = ast.value()[0]
            match felem.value():
                case "def!":
                    if felem.typ() == 3:
                        return repl_env.set(ast.value()[1], EVAL(ast.value()[2], repl_env))
                    else:
                        print("Error typ def!")
                        exit()
                case "let*":
                    if felem.typ() == 3:
                        new_env = env.Env(repl_env)
                        bindings = ast.value()[1]
                        if len(bindings.value()) % 2 == 1:
                            print("Bindings list not even length")
                            exit()
                        while bindings.nempty():
                            new_key = bindings.pop_first()
                            new_val = bindings.pop_first()
                            new_env.set(new_key.value(), EVAL(new_val, new_env))
                        return EVAL(ast.value()[2], new_env)
                case _:
                    val_ast = eval_ast(ast, repl_env)
                    fn = val_ast.pop(0)
                    return fn(val_ast)
        else:
            return ast
    else:
        return eval_ast(ast, repl_env)


def PRINT(input):
    return pr.pr_str(atom_as_mal_type(input))
    #return str(input)


def rep(input):
    repl_env = env.Env()
    for i in Base_functions.keys():
        repl_env.set(i, Base_functions[i])
    return PRINT(EVAL(READ(input), repl_env))


def main():
    while(True):
        try:
            line = input("user> ")
            print(rep(line))
        except EOFError:
            exit()


if __name__ == "__main__":
    main()
