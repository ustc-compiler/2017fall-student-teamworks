#!/usr/bin/env python3
# -- coding: utf8 --
# :author: nvagus
# :time: 12/22/17-3:47 PM
# :package: proto.test

import code

from proto import proto


@proto
def person(self, name):
    self._name = name


alice = person('Alice')


@alice.hook
def __new__(self, age):
    self._age = age


little_alice = alice(6)

code.interact(local=locals())
