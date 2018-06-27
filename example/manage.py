#!/usr/bin/env python
# coding=utf-8


import click
from flask.cli import FlaskGroup

from example.application import create_app_for_cli


@click.group(cls=FlaskGroup, create_app=create_app_for_cli)
def click_group():
    pass


if __name__ == '__main__':
    click_group()
