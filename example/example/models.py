#!/usr/bin/env python
# coding=utf-8


from flask_vises.database.models import GeneralObjectMixin, GeneralObjectQuery

from example.database import db


class GeneralObject(db.Model, GeneralObjectMixin):
    __abstract__ = False

    query_class = GeneralObjectQuery  # DON'T FORGET THIS LINE!
