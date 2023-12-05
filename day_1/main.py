from collections import defaultdict

DIGITS_NAME_TO_NUMBERS_MAP: dict[str, str] = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def main():
    with open('input.txt') as f:
        lines = f.readlines()

    result_sum = 0
    for line in lines:
        digits_indexes: list[tuple[int, str]] = []
        all_occurrences_of_keys: defaultdict[str, list[int]] = defaultdict(list)
        for key in DIGITS_NAME_TO_NUMBERS_MAP.keys():
            if key in line:
                start = 0
                end = len(line)
                key_len = len(key)
                while start + key_len <= end:
                    try:
                        idx_to_add = line.index(key, start, end)
                        all_occurrences_of_keys[key].append(idx_to_add)
                        start += idx_to_add + key_len
                    except ValueError:
                        break
                    print(all_occurrences_of_keys)

        for key, value in all_occurrences_of_keys.items():
            for idx in value:
                digits_indexes.append(
                    (
                        idx,
                        DIGITS_NAME_TO_NUMBERS_MAP[key]
                    )
                )

        for index, char in enumerate(line):
            if char.isdigit():
                digits_indexes.append(
                    (
                        index,
                        char
                    )
                )

        digits_indexes.sort(
            key=lambda item: item[0],
        )
        num_to_add = int(digits_indexes[0][1] + digits_indexes[-1][1])
        print(line, digits_indexes, num_to_add)
        result_sum += num_to_add

    print(result_sum)


if __name__ == '__main__':
    main()
