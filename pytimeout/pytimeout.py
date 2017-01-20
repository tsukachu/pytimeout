# -*- coding: utf-8 -*-

from functools import wraps
import signal


def _handler(signum, frame):
    raise TimeoutError


def timeout(sec):
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handler)
            signal.setitimer(signal.ITIMER_REAL, sec)
            try:
                return func(*args, **kwargs)
            finally:
                signal.setitimer(signal.ITIMER_REAL, 0)
        return wrapper
    return deco


def with_run(sec, func, *args, **kwargs):
    signal.signal(signal.SIGALRM, _handler)
    signal.setitimer(signal.ITIMER_REAL, sec)
    try:
        return func(*args, **kwargs)
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
