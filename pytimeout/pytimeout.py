# -*- coding: utf-8 -*-

from functools import wraps
import signal


def timeout(sec):
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            def handler(signum, frame):
                raise TimeoutError

            signal.signal(signal.SIGALRM, handler)
            signal.alarm(sec)
            try:
                return func(*args, **kwargs)
            finally:
                signal.alarm(0)
        return wrapper
    return deco


def with_run(sec, func, *args, **kwargs):
    def handler(signum, frame):
        raise TimeoutError

    signal.signal(signal.SIGALRM, handler)
    signal.alarm(sec)
    try:
        return func(*args, **kwargs)
    finally:
        signal.alarm(0)
