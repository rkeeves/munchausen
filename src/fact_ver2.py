#!/usr/bin/env python3


def fact_ver2(current, accu):
    print("fact_ver2({},{})".format(current, accu))
    if current < 2:
        return accu
    accu *= current
    if accu >= 5000:
        return 5000
    return fact_ver2(current - 1, accu)


def main():
    fact_ver2(8, 1)
    print("\nFinish")


##############################################################################

if __name__ == "__main__":
    main()
