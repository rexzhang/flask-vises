#!/usr/bin/env python
# coding=utf-8


import flask_testing
import sqlalchemy_utils


class TestCase(flask_testing.TestCase):
    def __init__(self, app, db):
        self.app = app
        self.db = db
        return

    def setUp(self):
        if not sqlalchemy_utils.database_exists(self.app.config.get('SQLALCHEMY_DATABASE_URI')):
            sqlalchemy_utils.create_database(self.app.config.get('SQLALCHEMY_DATABASE_URI'))

        self.db.create_all()
        return

    def tearDown(self):
        self.db.session.remove()

        # drop database
        # db.drop_all()  # this func can't work, so need sqlalchemy_utils
        if sqlalchemy_utils.database_exists(self.app.config.get('SQLALCHEMY_DATABASE_URI')):
            sqlalchemy_utils.drop_database(self.app.config.get('SQLALCHEMY_DATABASE_URI'))

        # re-create database
        sqlalchemy_utils.create_database(self.app.config.get('SQLALCHEMY_DATABASE_URI'))
        return


def configure_testing(app):
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False

    sqlalchemy_database = app.config.get('SQLALCHEMY_DATABASE')
    if sqlalchemy_database is not None:
        db_name = sqlalchemy_database.get('NAME')
        db_name_testing = sqlalchemy_database.get('NAME_TESTING')
        if db_name_testing is None and db_name is not None:
            sqlalchemy_database['NAME_TESTING'] = '{}_testing'.format(db_name)

    return
