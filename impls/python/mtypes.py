#!/usr/bin/env python3
class Mal:
    mtype = 0

    def value(self):
        pass

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
    symbol = ""

    def __init__(self, symbol=""):
        self.symbol = symbol
        self.mtype = 3

    def value(self):
        return self.symbol


class MalString(Mal):
    val = ""

    def __init__(self, input=""):
        self.val = input
        self.mtype = 4

    def value(self):
        return self.val


class MalKeyword(Mal):
    pass


class MalHashmap(Mal):
    pass


class MalVector(Mal):
    pass
