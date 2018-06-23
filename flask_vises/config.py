#!/usr/bin/env python
# coding=utf-8


class ConfigAbstract(object):
    SQLALCHEMY_DATABASE = {
        'ENGINE': 'postgresql',
        'NAME': None,
        'NAME_TESTING': None,
        'USER': None,
        'PASSWORD': None,
        'HOST': 'localhost',
        'PORT': None,
    }
    pass
