#!/usr/bin/env python
# coding=utf-8


import unittest

from flask_vises.password import generate_password_hash, check_password_hash


class TestPassword(unittest.TestCase):
    def test_password(self):
        password_list = ['abc', '123']

        for password in password_list:
            self.assertTrue(
                check_password_hash(hashed_password=generate_password_hash(password=password), password=password)
            )
        return


if __name__ == '__main__':
    unittest.main()
