#!/usr/bin/env python
# coding=utf-8


import flask

from example.models import GeneralOption

home_page = flask.Blueprint('views', __name__)


@home_page.route('/')
def home():
    value = GeneralOption.get_value(group='home', value=1)
    return '{}'.format(value)


@home_page.route('/add')
def home_add():
    value = GeneralOption.get_value(group='home')
    if value is None:
        value = 1

    GeneralOption.set_value(group='home', value=value + 1)
    return '{}'.format(value)
