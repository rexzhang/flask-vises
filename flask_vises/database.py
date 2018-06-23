#!/usr/bin/env python
# coding=utf-8


from flask_migrate import Migrate


def configure_db(app, db, enable_migrate=True):
    if app.config.get('SQLALCHEMY_DATABASE_URI') is None:
        sqlalchemy_database = app.config.get('SQLALCHEMY_DATABASE')
        if sqlalchemy_database is None:
            raise Exception('app.config missing SQLALCHEMY_DATABASE or SQLALCHEMY_DATABASE_URI')

        if set(list(['ENGINE', 'NAME', 'USER'])).issubset(set(sqlalchemy_database.keys())) is None:
            raise Exception('SQLALCHEMY_DATABASE missing key: ENGINE/NAME/USER')

        app.config.update({'SQLALCHEMY_DATABASE_URI': '{}://{}{}@{}{}/{}?client_encoding=utf8'.format(
            sqlalchemy_database['ENGINE'],
            sqlalchemy_database['USER'],
            '' if sqlalchemy_database.get('PASSWORD') is None else ':{}'.format(sqlalchemy_database['PASSWORD']),
            sqlalchemy_database['HOST'],
            '' if sqlalchemy_database.get('PORT') is None else ':{}'.format(sqlalchemy_database['PORT']),
            sqlalchemy_database['NAME']
        )})

    # init flask_sqlalchemy
    db.init_app(app)

    # init flask_migrate
    if enable_migrate:
        Migrate(app, db)
    return
