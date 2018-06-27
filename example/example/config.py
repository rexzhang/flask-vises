#!/usr/bin/env python
# coding=utf-8

from flask_vises.config import ConfigAbstract


class Config(ConfigAbstract):
    # Database
    ConfigAbstract.SQLALCHEMY_DATABASE['NAME'] = 'flask_vises_example'
    ConfigAbstract.SQLALCHEMY_DATABASE['USER'] = 'rex'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
