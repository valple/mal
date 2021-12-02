#!/usr/bin/env python3
import readline
import reader as rdr
import printer as pr
import mtypes as tp
import env
import core

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
            felem = ast.pop_first()
            match felem.value():
                case "def!":
                    if felem.typ() == 3:
                        return repl_env.set(ast.value()[0], EVAL(ast.value()[1], repl_env))
                    else:
                        print("Error typ def!")
                        exit()
                case "let*":
                    if felem.typ() == 3:
                        new_env = env.Env(outer=repl_env)
                        bindings = ast.value()[0]
                        if len(bindings.value()) % 2 == 1:
                            print("Bindings list not even length")
                            exit()
                        while bindings.nempty():
                            new_key = bindings.pop_first()
                            new_val = bindings.pop_first()
                            new_env.set(new_key.value(), EVAL(new_val, new_env))
                        return EVAL(ast.value()[1], new_env)
                case "do":
                    done = [EVAL(x, repl_env) for x in ast.value()]
                    return done[-1]
                case "if":
                    cond = ast.pop_first()
                    ifeval = ast.pop_first()
                    if eval_ast(cond, repl_env) not in ("nil", "false"):
                        return eval_ast(ifeval, repl_env)
                    elif ast.nempty():
                        return eval_ast(ast.pop_first(), repl_env)
                    else:
                        return tp.MalNil()
                case "fn*":
                    binds = [x.value() for x in ast.pop_first().value()]
                    body = ast.pop_first()
                    return lambda x: fn_maker(repl_env, binds, body, x)
                case _:
                    val_ast = eval_ast(ast, repl_env)
                    fn = EVAL(felem, repl_env)
                    return fn(val_ast)
        else:
            return ast
    else:
        return eval_ast(ast, repl_env)


def fn_maker(oenv, binds, body, exprs):
    new_env = env.Env(oenv, binds, exprs)
    return EVAL(body, new_env)


def PRINT(input):
    return pr.pr_str(atom_as_mal_type(input))
    # return str(input)


def rep(input):
    ns = core.ns()
    repl_env = env.Env()
    for i in ns.data.keys():
        repl_env.set(i, ns.data[i])
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
