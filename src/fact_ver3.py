#!/usr/bin/env python3


def fact_ver3(num):
    print("fact_ver3({})".format(num))

    def fact_ver2(current, accu):
        print("fact_ver2({},{})".format(current, accu))
        if current < 2:
            return accu
        accu *= current
        if accu >= 5000:
            return 5000
        return fact_ver2(current - 1, accu)

    return fact_ver2(num, 1)


def main():
    fact_ver3(8)
    print("\nFinish")


##############################################################################

if __name__ == "__main__":
    main()
