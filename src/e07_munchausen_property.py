#!/usr/bin/env python3

CACHE = [0] + [x ** x for x in range(1, 10)]


def is_munchausen(digit_counts, pow_sum):
    for digit_ch in str(pow_sum):
        digit = int(digit_ch)
        digit_counts[digit] -= 1
    for digit_count in digit_counts:
        if digit_count != 0:
            return False
    return True


def compute_pow_sum(digit_counts):
    return sum(
        digit_count * CACHE[digit] for digit, digit_count in enumerate(digit_counts)
    )


def test(digit_counts):
    digit_counts_copy = digit_counts[:]
    pow_sum = compute_pow_sum(digit_counts)
    is_munch = is_munchausen(digit_counts, pow_sum)
    print("{} -> {:4} -> {}".format(digit_counts_copy, pow_sum, is_munch))


def main():
    # 0
    test([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    # 1
    test([0, 1, 0, 0, 0, 0, 0, 0, 0, 0])
    # 3435
    test([0, 0, 0, 2, 1, 1, 0, 0, 0, 0])
    # 2021
    test([1, 1, 2, 0, 0, 0, 0, 0, 0, 0])


##############################################################################

if __name__ == "__main__":
    main()
