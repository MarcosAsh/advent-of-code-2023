from collections import Counter
import numpy as np

# set to true or false depending on answer wanted
IS_PART_ONE = False


def get_type_boost(hand):
    char_count = Counter(hand)
    most_common_count = char_count.most_common(1)[0][1]
    if not IS_PART_ONE and 'J' in char_count and len(char_count) > 1:
        most_common_count = char_count.pop('J', 0) + char_count.most_common(1)[0][1]
    num_unique_chars = len(char_count)
    match most_common_count:
        case 5:
            return '8'
        case 4:
            return '7'
        case 3:
            return '6' if num_unique_chars == 2 else '5'
        case 2:
            return '4' if num_unique_chars == 3 else '3'
        case _:
            return '2'


def base14_to_dec(hand):
    digits = '23456789TJQKA' if IS_PART_ONE else 'J23456789TQKA'
    return sum(digits.index(char) * (14 ** i) for i, char in enumerate(hand[::-1]))


def main():
    with open("input") as f:
        hands, bids = zip(
            *[(handstr, int(bidstr)) for handstr, bidstr in map(lambda line: line.strip().split(), f.readlines())])

    raw_ranks = []
    for hand in hands:
        raw_ranks.append(base14_to_dec(get_type_boost(hand) + hand))
    _, bids_sorted = zip(*sorted(zip(raw_ranks, bids), key=lambda x: x[0]))

    print(np.dot(np.arange(1, len(bids_sorted) + 1), bids_sorted))


if __name__ == "__main__":
    main()
