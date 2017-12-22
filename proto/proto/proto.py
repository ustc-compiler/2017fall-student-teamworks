#!/usr/bin/env python3
# -- coding: utf8 --
# :author: nvagus
# :time: 12/22/17-3:47 PM
# :package: proto

from types import MethodType


class Proto(type):
    def __new__(mcs, init, *args, **kwargs):
        obj = super(Proto, mcs).__new__(mcs, init.__name__, (mcs,), {})
        def __new__(cls, *args, **kwargs):
            obj = super(Proto, cls).__new__()

    def __setattr__(cls, key, value):
        print(key, value)
        super(Proto, cls).__setattr__(key, value)


def proto(base=Proto):
    def __proto__(f):
        def _wrapper(*args, **kwargs):
            obj = base(f, )
        return _wrapper

    return __proto__
