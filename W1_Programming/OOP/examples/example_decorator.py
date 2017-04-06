# Code taken from Fluent Python by Luciano Ramalho
# See Example 7-15, page 199

import time

def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('{:.8f} {}({}) -> {}'.format(elapsed, name, arg_str, result))
        return result
    return clocked


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)


if __name__=='__main__':
    snooze(.5)
    print('*' * 40)
    factorial(6)
