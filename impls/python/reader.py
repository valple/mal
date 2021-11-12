#!/usr/bin/env python3
#
import re
import mtypes as tp


FLOAT_REGEX = "-?(([1-9]+[0-9]*)\\.[0-9]*)?|(0\\.[0-9]*)"
MAL_REGEX = "[\\s,]*(~@|[\\[\\]{}()'`~^@]|\"(?:\\.|[^\\\"])*\"?|;.*|[^\\s\\[\\]{}('\"`,;)]*)"


class Reader():
    tokens = []

    def peek(self):
        return self.tokens[0]

    def next(self):
        token = self.tokens[0]
        self.tokens.pop(0)
        return token
    # feels like cheating
    # filter to get rid of whitespaces that python regex likes to capture

    def __init__(self, line):
        self.tokens = list(filter(None, re.findall(MAL_REGEX, line)))


def read_atom(reader):
    token = reader.peek()
    # switch statement later for more advanced types
    # also implement integer etc
    if token[0].isdigit() and re.match(FLOAT_REGEX, token):
        return tp.MalNumber(float(token))
    else:
        return tp.MalSymbol(token)


def read_form(reader):
    token = reader.peek()
    if token == "(":
        return read_list(reader)
    else:
        return read_atom(reader)


def read_list(reader):
    reader.next()
    malist = tp.MalList()

    while(reader.tokens):
        token = reader.peek()
        if token == ")":
            return malist
        else:
            malist.lappend(read_form(reader))
            reader.next()
    # Implement error
    return 0


def read_str(content):
    reader = Reader(content)
    return read_form(reader)
