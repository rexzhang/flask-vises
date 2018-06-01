#!/usr/bin/env python
# coding=utf-8


from uuid import uuid4
from sqlalchemy import Column, DateTime, func, Numeric, Integer
from decimal import Decimal
from sqlalchemy.dialects.postgresql import UUID

from database import db

__all__ = ['BaseModelObject', 'BaseModelRecord']


class BaseModel(db.Model):
    __abstract__ = True

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    created_time = Column(
        DateTime(timezone=True),
        nullable=False,
        default=func.now(),
    )

    def to_dict(self):
        """convert object to python dict"""
        result = {}
        for col in self.__table__.columns:
            if isinstance(col.type, Numeric):
                value = getattr(self, col.name) if getattr(self, col.name) else Decimal(0.00)
            elif isinstance(col.type, Integer):
                value = getattr(self, col.name) if getattr(self, col.name) else 0
            else:
                value = getattr(self, col.name, None)
            result[col.name] = value

        return result

    def update_from_dict(self, obj_dict):
        """update object from python dict """
        try:
            obj_id = obj_dict.pop('id')
            obj_key_list = obj_dict.keys()

            if self.query.filter_by(id=obj_id).count() != 1:
                # don't create new record
                raise KeyError

        except KeyError:
            return False

        for c in self.__table__.columns:
            if c.name not in obj_key_list:
                continue

            value = obj_dict.get(c.name, None)
            if value is None:
                continue

            setattr(self, c.name, value)
        return True

    def __repr__(self):
        """don't forget overload!"""
        return '{}'.format(self.id)


class BaseModelObject(BaseModel):
    """base model - Object"""
    __abstract__ = True

    # last update time
    updated_time = Column(
        DateTime(timezone=True),
        nullable=False,
        default=func.now(),
        onupdate=func.now(),
    )


class BaseModelRecord(BaseModel):
    """base model - record/log"""
    __abstract__ = True
