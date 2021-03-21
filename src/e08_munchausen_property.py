#!/usr/bin/env python3

import time

CACHE = [0] + list(x ** x for x in range(1, 10))


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


def list_munchausens_of_decimal_places(decimal_places):
    ret = []

    if decimal_places < 1:
        return ret

    def assign_count(digit_counts, remaining_count):
        if len(digit_counts) == 10:
            pow_sum = compute_pow_sum(digit_counts)
            if is_munchausen(digit_counts, pow_sum):
                ret.append(pow_sum)
            return
        from_num = 0
        if len(digit_counts) == 9:
            from_num = remaining_count
        for chosen_count in range(from_num, remaining_count + 1):
            assign_count(digit_counts + [chosen_count], remaining_count - chosen_count)

    assign_count([], decimal_places)
    return ret


def list_munchausens_up_to_decimal_places(max_decimal_places):
    accu = []
    for decimal_places in range(1, max_decimal_places + 1):
        accu += list_munchausens_of_decimal_places(decimal_places)
    return sorted(accu)


def test(decimal_places):
    elapsed = time.time()
    munchausen_nums = list_munchausens_up_to_decimal_places(decimal_places)
    elapsed = time.time() - elapsed
    print(
        "{:.6f}s Decimals places: {:2} -> {}".format(
            elapsed, decimal_places, munchausen_nums
        )
    )


def main():
    for decimal_places in range(1, 12):
        test(decimal_places)
    print("Finished")


##############################################################################

if __name__ == "__main__":
    main()
