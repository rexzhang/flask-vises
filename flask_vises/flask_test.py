#!/usr/bin/env python
# coding=utf-8


import flask_testing
import sqlalchemy_utils

from application import create_app_for_testing, db


class TestCase(flask_testing.TestCase):
    def create_app(self):
        self.db = db
        self.app = create_app_for_testing()
        return self.app

    def setUp(self):
        if not sqlalchemy_utils.database_exists(self.app.config.get('SQLALCHEMY_DATABASE_URI')):
            sqlalchemy_utils.create_database(self.app.config.get('SQLALCHEMY_DATABASE_URI'))

        db.create_all()
        return

    def tearDown(self):
        db.session.remove()

        # drop database
        # db.drop_all()  # this func can't work, so need sqlalchemy_utils
        if sqlalchemy_utils.database_exists(self.app.config.get('SQLALCHEMY_DATABASE_URI')):
            sqlalchemy_utils.drop_database(self.app.config.get('SQLALCHEMY_DATABASE_URI'))

        # re-create database
        sqlalchemy_utils.create_database(self.app.config.get('SQLALCHEMY_DATABASE_URI'))
        return
