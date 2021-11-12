#!/usr/bin/env python3
import readline


def READ(input):
    return input


def EVAL(input):
    return input


def PRINT(input):
    return input


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
