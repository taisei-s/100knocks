# coding:utf-8

import re

def cipher(str):
    pattern = r'[a-z]'
    prog = re.compile(pattern)
    encoded = ''
    for c in str:
        encoded += chr(219-ord(c)) if prog.match(c) else c

    return encoded


def swing08(str):
    encoded = cipher(str)
    decoded = cipher(encoded)

    return encoded, decoded


if __name__ == "__main__":
    str = 'Hello, Python World.'
    print(swing08(str))