#!/usr/bin/env python
# coding=utf-8


from uuid import uuid4
from sqlalchemy import Column, DateTime, String, func
from sqlalchemy.dialects import postgresql
from flask_sqlalchemy import BaseQuery

GENERAL_OBJECT_TABLE_NAME = 'general_object'


class AbstractModelMixin(object):
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


class ObjectModelMixin(AbstractModelMixin):
    """model mixin - Object"""
    __abstract__ = True

    # last update time
    updated_time = Column(
        DateTime(timezone=True),
        nullable=False,
        default=func.now(),
        onupdate=func.now(),
    )


class RecordModelMixin(AbstractModelMixin):
    """model mixin - Record/Logging"""
    __abstract__ = True


class GeneralObjectQuery(BaseQuery):
    def set_value(self, general_object_model_class, group, key=None, value=None):
        """set|create/update"""
        if key is None:
            key = group

        obj = self.get_queryset_by_group_and_key(group=group, key=key).first()
        if obj is None:
            obj = general_object_model_class(
                group=group,
                key=key,
                value=value
            )

        else:
            obj.value = value

        self.session.add(obj)
        self.session.commit()
        return obj

    def get_value(self, group, key=None):
        """get value"""
        if key is None:
            key = group

        obj = self.get_queryset_by_group_and_key(group=group, key=key).first()

        if obj is None:
            return None

        return obj.value

    def get_object(self, group, key=None):
        """get object"""
        return self.get_queryset_by_group_and_key(group=group, key=key).first()

    def get_queryset_by_group_and_key(self, group, key=None):
        """get queryset"""
        if key is None:
            return self.filter_by(group=group)

        else:
            return self.filter_by(group=group, key=key)


class GeneralObjectMixin(ObjectModelMixin):
    __abstract__ = True
    __tablename__ = GENERAL_OBJECT_TABLE_NAME
    query_class = GeneralObjectQuery

    group = Column(
        String(20),
        server_default='',
        nullable=False,
    )
    key = Column(
        String(50),
        server_default='',
        nullable=False,
    )
    value = Column(
        postgresql.JSONB,
    )

    @classmethod
    def set_value(cls, group, key=None, value=None):
        """set|create/update"""
        return cls.query.set_value(general_object_model_class=cls, group=group, key=key, value=value)

    @classmethod
    def get_value(cls, group, key=None):
        """get value"""
        return cls.query.get_value(group=group, key=key)

    def __repr__(self):
        return '<GeneralObject:{}|{}>'.format(self.id, self.key)
