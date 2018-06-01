#!/usr/bin/env python
# coding=utf-8


import redis

# Find the stack on which we want to store the database connection.
# Starting with Flask 0.9, the _app_ctx_stack is the correct one,
# before that we need to use the _request_ctx_stack.
try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack


class FlaskRedis(object):

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.app = app
        redis_urls = app.config.get('REDIS_URLS')

        if not hasattr(app.extensions, 'redis'):
            app.extensions['redis'] = {}

        for k, v in redis_urls.items():
            app.extensions['redis'][k] = redis.Redis().from_url(v)

    def get_connection(self, redis_prefix):
        """Return Redis connection for current app."""
        return self.get_app().extensions['redis'][redis_prefix]

    def get_app(self):
        """Get current app from Flask stack to use.
        This will allow to ensure which Redis connection to be used when
        accessing Redis connection public methods via plugin.
        """
        # First see to connection stack
        ctx = stack.top
        if ctx is not None:
            return ctx.app

        # Next return app from instance cache
        if self.app is not None:
            return self.app

        # Something went wrong, in most cases app just not instantiated yet
        # and we cannot locate it
        raise RuntimeError(
            'Flask application not registered on Redis instance '
            'and no applcation bound to current context')
