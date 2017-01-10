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


if __name__ == '__main__':
    unittest.main()