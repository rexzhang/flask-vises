#!/usr/bin/env python
# coding=utf-8


from flask_vises.database.models import GeneralOptionMixin

from example.database import db


class GeneralOption(db.Model, GeneralOptionMixin):
    __abstract__ = False
