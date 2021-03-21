#!/usr/bin/env python3


def list_munchausens_of_decimal_places(decimal_places):
    ret = [0]

    if decimal_places < 1:
        return ret

    def assign_count(digit_counts, remaining_count):
        if len(digit_counts) == 10:
            ret[0] += 1
            return
        from_num = 0
        if len(digit_counts) == 9:
            from_num = remaining_count
        for chosen_count in range(from_num, remaining_count + 1):
            assign_count(digit_counts + [chosen_count], remaining_count - chosen_count)

    assign_count([], decimal_places)
    return ret[0]


def list_munchausens_up_to_decimal_places(max_decimal_places):
    total_case_count = 0
    for decimal_places in range(1, max_decimal_places + 1):
        total_case_count += list_munchausens_of_decimal_places(decimal_places)
    print("{:2} -> {}".format(max_decimal_places, total_case_count))
    return total_case_count


def main():
    print("max_decimal_places -> total_case_count")
    for decimal_places in range(1, 12):
        list_munchausens_up_to_decimal_places(decimal_places)
    print("Finished")


##############################################################################

if __name__ == "__main__":
    main()
