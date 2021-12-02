#!/usr/bin/env python3
import printer as pr
import mtypes as tp


class ns:
    data = {'+': lambda a: mal_sum(a),
            '-': lambda a: mal_diff(a),
            '*': lambda a: mal_prod(a),
            '/': lambda a: mal_div(a)}

    def prn(self, *args):
        print(pr.pr_str(args[0]))
        return tp.MalNil()

    def list(self, *args):
        return list(args)

    def islist(self, *args):
        return isinstance(args[0], list)

    def isempty(self, *args):
        return not args[0]

    def count(self, *args):
        return len(args[0])

    def equal(self, *args):
        if type(args[0]) is type(args[1]):
            return args[0] == args[1]
        else:
            return False

    def lequal(self, *args):
        return args[0] <= args[1]

    def less(self, *args):
        return args[0] < args[1]

    def mequal(self, *args):
        return args[0] >= args[1]

    def more(self, *args):
        return args[0] > args[1]


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
