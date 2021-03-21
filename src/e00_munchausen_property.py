#!/usr/bin/env python3

import time


def is_munchausen(num):
    accu = 0
    for digit_char in str(num):
        digit = int(digit_char)
        accu += digit ** digit
    return accu == num


def test(func_to_apply, func_arg):
    delta = time.time()
    ret = func_to_apply(func_arg)
    delta = time.time() - delta
    print("[{:.6f}s] {} -> {}".format(delta, func_arg, ret))


def main():
    for num in [0, 1, 2021, 3435]:
        test(is_munchausen, num)


##############################################################################

if __name__ == "__main__":
    main()
