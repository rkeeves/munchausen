#!/usr/bin/env python3

import time


def is_munchausen(num):
    accu = 0
    for digit_char in str(num):
        digit = int(digit_char)
        accu += 0 if digit == 0 else digit ** digit
    return accu == num


def list_munchausen(up_to):
    accu = []
    for num in range(0, up_to):
        if is_munchausen(num):
            accu.append(num)
    return accu


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
