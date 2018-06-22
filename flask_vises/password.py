#!/usr/bin/env python
# coding=utf-8


from werkzeug.security import (
    generate_password_hash as werkzeug_generate_password_hash,
    check_password_hash as werkzeug_check_password_hash,
)

__all__ = ['generate_password_hash', 'check_password_hash']


def generate_password_hash(password):
    return werkzeug_generate_password_hash(password=bytes(password.encode('utf-8')), method='pbkdf2:sha256:50000')


def check_password_hash(hashed_password, password):
    return werkzeug_check_password_hash(pwhash=hashed_password, password=bytes(password.encode('utf-8')))
