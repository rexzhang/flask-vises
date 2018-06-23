#!/usr/bin/env python
# coding=utf-8


class ConfigAbstract(object):
    SQLALCHEMY_DATABASE = {
        'ENGINE': 'postgresql',
        'NAME': None,
        'USER': None,
        'PASSWORD': None,
        'HOST': 'localhost',
        'PORT': None,
    }
    pass
