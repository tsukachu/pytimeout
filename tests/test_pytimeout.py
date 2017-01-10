# -*- coding: utf-8 -*-

import time
import unittest

from pytimeout import pytimeout


class TestPytimeout(unittest.TestCase):
    def test_timeout(self):
        @pytimeout.timeout(1)
        def func():
            time.sleep(1.1)

        with self.assertRaises(TimeoutError):
            func()

    def test_timeout_not_raise(self):
        @pytimeout.timeout(1)
        def func():
            return True

        self.assertTrue(func())

    def test_with_run(self):
        def func():
            time.sleep(1.1)

        with self.assertRaises(TimeoutError):
            pytimeout.with_run(1, func)

    def test_with_run_not_raise(self):
        def func():
            return True

        self.assertTrue(pytimeout.with_run(1, func))


if __name__ == '__main__':
    unittest.main()
