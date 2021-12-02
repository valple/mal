#!/usr/bin/env python3
class Mal:
    mtype = 0
    val = 0

    def value(self):
        return self.val

    def typ(self):
        return self.mtype


class MalList(Mal):
    mlist = []

    def __init__(self, nlist=None):
        if nlist is None:
            self.mlist = []
        else:
            self.mlist = nlist
        self.mtype = 1

    def value(self):
        return self.mlist

    def lappend(self, item):
        return self.mlist.append(item)

    def pop_first(self):
        return self.mlist.pop(0)

    def nempty(self):
        return bool(self.mlist)


class MalNumber(Mal):
    number = 0

    def __init__(self, number=0):
        self.number = number
        self.mtype = 2

    def value(self):
        return self.number


class MalSymbol(Mal):
    val = ""

    def __init__(self, symbol=""):
        self.val = symbol
        self.mtype = 3

    def value(self):
        return self.val


class MalString(Mal):
    val = '""'

    def __init__(self, input=""):
        self.val = input
        self.mtype = 4

    def value(self):
        return self.val


class MalNil(Mal):
    val = "nil"

    def __init__(self):
        self.mtype = 5


class MalBool(Mal):
    val = ""

    def __init__(self):
        self.mtype = 6

    def value(self):
        return self.val


class MalTrue(MalBool):
    val = "true"

    def __init__(self):
        self.val = "true"
        self.mtype = 6


class MalFalse(MalBool):
    val = "false"

    def __init__(self):
        self.val = "false"
        self.mtype = 6


class MalKeyword(Mal):
    pass


class MalHashmap(Mal):
    pass


class MalVector(Mal):
    pass
