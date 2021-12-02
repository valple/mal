#!/usr/bin/env python3
import mtypes as tp


class Env:
    data = {}
    outer = tp.MalNil()

    def __init__(self, outer=None, binds=None, exprs=None):
        self.data = {}
        if outer is None:
            self.outer = tp.MalNil()
        else:
            self.outer = outer
        while binds:
            key = binds.pop(0)
            val = exprs.pop(0)
            self.set(key, val)

    def set(self, key, mal):
        self.data[key] = mal
        return mal

    def find(self, key):
        if key in self.data.keys():
            return self
        elif isinstance(self.outer, (tp.Mal, tp.MalNil)):
            return False
        else:
            return self.outer.find(key)

    def get(self, key):
        if self.find(key):
            return self.find(key).data[key]
        else:
            print("Key not found: ", key)
            exit()
