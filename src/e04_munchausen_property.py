#!/usr/bin/env python3

import time


def is_munchausen(num):
    return sum(0 if ch == "0" else int(ch) ** int(ch) for ch in str(num)) == num


def list_munchausen(up_to):
    return [num for num in range(0, up_to) if is_munchausen(num)]


def test(func_to_apply, func_arg):
    delta = time.time()
    ret = func_to_apply(func_arg)
    delta = time.time() - delta
    print("[{:.6f}s] {:7d} -> {}".format(delta, func_arg, ret))


def main():
    for num in [1, 10, 100, 1000, 10000, 100000, 1000000]:
        test(list_munchausen, num)


##############################################################################

if __name__ == "__main__":
    main()
