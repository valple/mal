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
    while True:
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
                            ast = ast.value()[1]
                            repl_env = new_env
                            continue
                            # return EVAL(ast.value()[1], new_env)
                    case "do":
                        done = [EVAL(x, repl_env) for x in ast.value()[0:len(ast.value())-1]]
                        ast = ast.value()[-1]
                        continue
                    case "if":
                        cond = ast.pop_first()
                        # ifeval = ast.pop_first()
                        if eval_ast(cond, repl_env) not in ("nil", "false"):
                            # return eval_ast(ifeval, repl_env)
                            ast = ast.value()[0]
                            continue
                        elif ast.nempty():
                            # return eval_ast(ast.pop_first(), repl_env)
                            ast = ast.value()[1]
                            continue
                        else:
                            return tp.MalNil()
                    case "fn*":
                        binds = [x.value() for x in ast.pop_first().value()]
                        body = ast.pop_first()
                        fun = fn_maker(repl_env, binds, body)
                        return malfn(body, binds, repl_env, fun)
                    case _:
                        val_ast = eval_ast(ast, repl_env)
                        fn = EVAL(felem, repl_env)
                        if isinstance(fn, malfn):
                            ast = fn.ast
                            repl_env = env.Env(repl_env, fn.params, val_ast)
                            continue
                        else:
                            return fn(val_ast)
            else:
                return ast
        else:
            return eval_ast(ast, repl_env)


class malfn:
    ast = tp.Mal()
    params = tp.Mal()
    env = env.Env()
    fn = tp.MalNil()

    def __init__(self, ast, params, env, fn):
        self.ast = ast
        self.params = params
        self.env = env
        self.fn = fn


def fn_maker(oenv, binds, body):
    return lambda x: fn_maker_helper(oenv, binds, body, x)


def fn_maker_helper(oenv, binds, body, exprs):
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
