#!/usr/bin/env python3
import readline
import reader as rdr
import printer as pr


def READ(input):
    return rdr.read_str(input)


def EVAL(input):
    return input


def PRINT(input):
    return pr.pr_str(input)


def rep(input):
    return PRINT(EVAL(READ(input)))


def main():
    while(True):
        try:
            line = input("user> ")
            print(rep(line))
        except EOFError:
            exit()


if __name__ == "__main__":
    main()
