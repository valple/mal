#!/usr/bin/env python3
import types as tp


def pr_str(mal, print_readably=True):
    output = ""
    match mal.typ():
        case 6:
            return mal.value()
        case 5:
            return mal.value()
        case 4:
            return mal.value()
        case 3:
            return mal.value()
        case 2:
            return str(mal.value())
        case 1:
            output += "("
            while mal.nempty():
                nmal = mal.pop_first()
                output += pr_str(nmal)
                if mal.nempty():
                    output += " "
            output += ")"
            return output
        # other cases later
        case _:
            return "hahahah"
