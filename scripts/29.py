import hashlib
import os
import random
import string
import secrets


def gen_random(length, chars):
    return ''.join(random.choice(chars) for _ in range(length))


def gen_secrets(length, chars):
    return ''.join(secrets.choice(chars) for _ in range(length))


def func_1():
    return gen_random(
        20,
        string.digits + string.ascii_lowercase + string.ascii_uppercase
    )


def func_2():
    return gen_secrets(
        20,
        string.digits + string.ascii_lowercase + string.ascii_uppercase
    )


def func_3():
    return gen_random(20, string.ascii_letters + string.digits + '_')


def func_4():
    return gen_secrets(20, string.ascii_letters + string.digits + '_')


def func_5():
    chars = ''.join(
        c for c in string.ascii_letters + string.digits + '_'
        if c not in 'O0l1I'
    )
    return gen_random(20, chars)


def func_6():
    chars = ''.join(
        c for c in string.ascii_letters + string.digits + '_'
        if c not in 'O0l1I'
    )
    return gen_secrets(20, chars)


def func_7():
    return hashlib.sha256(os.urandom(32)).hexdigest()[:20]


if __name__ == '__main__':
    print(func_1())
    print(func_2())
    print(func_3())
    print(func_4())
    print(func_5())
    print(func_6())
    print(func_7())
