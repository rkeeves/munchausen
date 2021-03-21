#!/usr/bin/env python3


def fact_ver1(num):
    print("fact_ver1({})".format(num))
    if num < 2:
        return 1
    ret = num * fact_ver1(num - 1)
    if ret >= 5000:
        return 5000
    return ret


def main():
    fact_ver1(8)
    print("\nFinish")


##############################################################################

if __name__ == "__main__":
    main()
