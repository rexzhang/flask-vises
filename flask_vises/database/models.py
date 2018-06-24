#!/usr/bin/env python
# coding=utf-8


from uuid import uuid4
from sqlalchemy import Column, DateTime, func
from sqlalchemy.dialects import postgresql


class ModelMixinAbstract(object):
    __abstract__ = True

    id = Column(
        postgresql.UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    created_time = Column(
        DateTime(timezone=True),
        nullable=False,
        default=func.now(),
    )

    def __repr__(self):
        """don't forget overload!"""
        return '{}'.format(self.id)


class ObjectModelMixin(ModelMixinAbstract):
    """model mixin - Object"""
    __abstract__ = True

    # last update time
    updated_time = Column(
        DateTime(timezone=True),
        nullable=False,
        default=func.now(),
        onupdate=func.now(),
    )


class RecordModelMixin(ModelMixinAbstract):
    """model mixin - Record/Logging"""
    __abstract__ = True
