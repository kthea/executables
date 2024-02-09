#!/usr/bin/env python

from datetime import datetime as dt


def gen_simple_id() -> str:
    return 'D' + str(dt.now().replace(microsecond=0)).replace(' ', 'H')


if __name__ == '__main__':
    print(gen_simple_id())
