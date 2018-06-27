#!/usr/bin/env python
# coding=utf-8


import flask

from example.models import GeneralObject

home_page = flask.Blueprint('views', __name__)


@home_page.route('/')
def home():
    value = GeneralObject.get_value(group='home')
    return '{}'.format(value)


@home_page.route('/add')
def home_add():
    value = GeneralObject.get_value(group='home')
    if value is None:
        value = 1

    GeneralObject.set_value(group='home', value=value + 1)
    return '{}'.format(value)
