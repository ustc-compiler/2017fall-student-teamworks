#!/usr/bin/env python3
# -- coding: utf8 --
# :author: nvagus
# :time: 12/22/17-3:47 PM
# :package: proto


class Type:
    def method(self):
        pass


instance = Type()
method = type(instance.method)
unbounded = type(Type.method)


class Proto(type):
    @classmethod
    def __attr__(mcs, _):
        yield from ()

    def __new__(mcs, *args, **kwargs):
        def __attr__(cls, item):
            result = cls.__proto__.get(item)
            if result is not None:
                yield result
            for __super__ in cls.__super__:
                yield from __super__.__attr__(item)

        obj = super(Proto, mcs).__new__(
            mcs, kwargs.pop('__name__'), (mcs,),
            {
                '__proto__': {},
                '__super__': [mcs],
                '__attr__': __attr__
            }
        )
        obj.__attr__ = method(obj.__attr__, obj)
        return obj

    def __init__(cls, *args, **kwargs):
        # pseudo super call
        super(Proto, cls).__init__(cls, None)
        # cls.__init_proto__(*args, **kwargs)

    def __setattr__(cls, key, value):
        print(key, value)
        cls.__proto__[key] = value

    def __getattr__(cls, item):
        print(item)
        try:
            return next(cls.__attr__(item))
        except StopIteration:
            pass
        raise AttributeError(item)


def proto(base=Proto):
    def __proto__(f):
        obj = base(__name__=f.__name__)
        return obj

    return __proto__
