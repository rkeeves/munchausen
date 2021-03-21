#!/usr/bin/env python3

import time

CACHE = [0] + list(x ** x for x in range(1, 10))


def is_munchausen_old(num):
    accu = 0
    for digit_char in str(num):
        digit = int(digit_char)
        accu += 0 if digit == 0 else digit ** digit
    return accu == num


def list_munchausen_old(up_to):
    accu = []
    for num in range(0, up_to):
        if is_munchausen_old(num):
            accu.append(num)
    return accu


def is_munchausen(num):
    accu = 0
    for digit_char in str(num):
        digit = int(digit_char)
        accu += CACHE[digit]
    return accu == num


def list_munchausen(up_to):
    accu = []
    for num in range(0, up_to):
        if is_munchausen(num):
            accu.append(num)
    return accu


def main():

    max_run_count = 50
    print("Started running both old and new version.")
    print(
        "Each of them will be called {} times, so this will take a while...".format(
            max_run_count
        )
    )
    delta = time.time()
    for run_count in range(0, max_run_count + 1):
        list_munchausen_old(100000)
    delta = time.time() - delta
    print(
        "Ran {:28} {} times, runtime: {:10.6f}s, avg runtime: {:10.6f}s".format(
            "list_munchausen_old(100000)", max_run_count, delta, delta / max_run_count
        )
    )
    delta = time.time()
    for run_count in range(0, max_run_count + 1):
        list_munchausen(100000)
    delta = time.time() - delta
    print(
        "Ran {:28} {} times, runtime: {:10.6f}s, avg runtime: {:10.6f}s".format(
            "list_munchausen(100000)", max_run_count, delta, delta / max_run_count
        )
    )
    print("Finished")


##############################################################################

if __name__ == "__main__":
    main()
