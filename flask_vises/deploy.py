#!/usr/bin/env python
# coding=utf-8


from enum import IntEnum, unique


@unique
class DeployLevel(IntEnum):
    develop = 1
    ci = 2
    test = 3
    alpha = 4
    beta = 5
    release = 6
