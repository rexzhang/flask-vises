#!/usr/bin/env python
# coding=utf-8


from flask import Flask
from flask_vises.database import configure_db

from example.config import Config
from example.database import db
from example import views


def create_app(testing=False):
    app = Flask('example')
    app.config.from_object(Config())

    configure_db(app, db)

    app.register_blueprint(views.home_page)
    return app


def create_app_for_cli(script_info):
    return create_app()


def create_app_for_testing():
    return create_app(testing=True)
