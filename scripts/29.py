import hashlib
import os
import random
import string


def gen(length, chars):
    return ''.join(random.choice(chars) for _ in range(length))


def func_1():
    return gen(
        20,
        string.digits + string.ascii_lowercase + string.ascii_uppercase
    )


def func_2():
    return hashlib.sha256(os.urandom(32)).hexdigest()[:20]


def func_3():
    return gen(20, string.ascii_letters + string.digits + '_')


if __name__ == '__main__':
    print(func_1())
    print(func_2())
    print(func_3())
